# 🎥 YouTube Trending Data Analytics Pipeline (AWS + Power BI)

An end-to-end **Data Engineering Pipeline** built on **AWS** to process, transform, analyze, and visualize YouTube Trending datasets.

---

## 📖 Overview

This project demonstrates how a scalable cloud-based data pipeline can be built using AWS services. Raw YouTube Trending data is ingested into Amazon S3, transformed into Parquet format using AWS Lambda, cataloged with AWS Glue, queried using Amazon Athena, and finally visualized through interactive dashboards in **Power BI**.

---

## 🏗️ Project Architecture


                Raw JSON / CSV Data
                        │
                        ▼
              Amazon S3 (Raw Layer)
                        │
          S3 Event Notification Trigger
                        │
                        ▼
                  AWS Lambda
            (Python + AWS Wrangler)
                        │
                        ▼
          Data Cleaning & Transformation
                        │
                        ▼
             Parquet Files (S3)
                        │
                        ▼
             AWS Glue Data Catalog
                        │
                        ▼
             Amazon Athena Queries
                        │
                        ▼
              Power BI Dashboard




## ✨ Features

- Automated data ingestion
- Event-driven ETL using AWS Lambda
- JSON to Parquet transformation
- Metadata management using AWS Glue Catalog
- SQL-based analysis with Amazon Athena
- Interactive Power BI dashboards
- Scalable cloud-based data lake architecture

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| **Language** | Python |
| **Libraries** | Pandas, AWS Wrangler |
| **Storage** | Amazon S3 |
| **Compute** | AWS Lambda |
| **Metadata** | AWS Glue |
| **Query Engine** | Amazon Athena |
| **Visualization** | Power BI |

---

## ☁️ AWS Services Used

### 🪣 Amazon S3
Stores raw datasets and transformed Parquet files in the data lake.

### ⚡ AWS Lambda
Automatically executes the ETL pipeline whenever new data is uploaded to S3.

### 📚 AWS Glue
Maintains schema information through the Glue Data Catalog.

### 🔍 Amazon Athena
Runs SQL queries directly on data stored in Amazon S3.

### 🔐 AWS IAM
Provides secure access management for AWS resources.

---

## 🔄 ETL Workflow

1. Upload raw YouTube dataset to **Amazon S3**.
2. **S3 Event Notification** triggers AWS Lambda.
3. Lambda reads the data using **AWS Wrangler**.
4. Data is cleaned and transformed.
5. Processed data is converted into **Parquet** format.
6. Parquet files are stored in the **S3 Cleansed Layer**.
7. AWS Glue updates the Data Catalog.
8. Amazon Athena performs SQL analysis.
9. Power BI connects to the processed data to create interactive dashboards.
