import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality
from awsglue.dynamicframe import DynamicFrame

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read from Glue Catalog
datasource0 = glueContext.create_dynamic_frame.from_catalog(
    database="de_youtube_raw_data",
    table_name="raw_statistics",
    transformation_ctx="datasource0",
    push_down_predicate="region in ('ca','gb','us')"
)

# Data Quality Rules
dq_ruleset = """
Rules = [
    RowCount > avg(last(10))*0.6,
    ColumnCount >= max(last(1))
]
"""

dq_result = EvaluateDataQuality().process_rows(
    frame=datasource0,
    ruleset=dq_ruleset,
    publishing_options={
        "dataQualityEvaluationContext": "youtube_raw_statistics",
        "enableDataQualityResultsPublishing": True
    },
    additional_options={
        "performanceTuning.caching": "CACHE_NOTHING"
    }
)

# Extract original data
original_data = SelectFromCollection.apply(
    dfc=dq_result,
    key="originalData",
    transformation_ctx="original_data"
)

# Convert to DataFrame
df = original_data.toDF()

# Optional: reduce number of output files
df = df.coalesce(1)

# Convert back to DynamicFrame
final_df = DynamicFrame.fromDF(
    df,
    glueContext,
    "final_df"
)

# Write parquet partitioned by region
glueContext.write_dynamic_frame.from_options(
    frame=final_df,
    connection_type="s3",
    format="glueparquet",
    connection_options={
        "path": "s3://de-on-youtube-cleandata-1/youtube/raw_statistics/",
        "partitionKeys": ["region"]
    },
    format_options={
        "compression": "snappy"
    },
    transformation_ctx="datasink"
)

job.commit()