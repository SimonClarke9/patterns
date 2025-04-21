# Data Platform Using AWS #

## Summary ##
Use AWS Cloud to build a Data Platform. In this Data Platform we want to manage streaming data like Clicks, other structured data, and Unstructured data
## Assumptions ##
| Question | Assumtion |
| :--- | :---|
| What data is to be ingested | Let's assume Structured data will be csv or JSON. <br> Unstructured Data will be images, binary files, text files |
| How often does data need to be ingested |  For Steaming Data, assume 15 minutes latency. <br> For Batch collection, assume 1hr intervals |

# Architecture #
<detials>
<summary>Explain  with  top level diagram the Tools to be used.</summary>
```Python
import image as architecture
```
</details>


# Data Ingestion #
Use AWS services like Kinesis Data Streams or AWS Glue to ingest data from sources like website clickstreams, purchase history, product catalogs, and user demographics.

## Collecting Data ##

## ETL Processes ##
### Cleaning ###
Ensure data is cleaned
### Transformation ###
transformed during ingestion to maintain consistency.

 


# Data Storage #
Store raw and processed data in Amazon S3 buckets, organized by data type and usage (e.g., raw data, processed data, analytics-ready data).

Use S3 lifecycle policies to manage storage costs by archiving older data to Amazon Glacier.

# Scalable Pipelines #
Implement ETL pipelines using AWS Glue or Apache Spark on Amazon EMR for processing large datasets.

Automate pipeline workflows with AWS Step Functions.

# Data Analytics #
Use Amazon Redshift or Athena for querying and analyzing data stored in S3.

Integrate with Amazon QuickSight for visualization and reporting.

# Machine Learning Integration #
Prepare data for machine learning models using Amazon SageMaker.

Train and deploy recommendation models that leverage user behavior and product data.

# Security and Governance #
Implement access controls using AWS IAM and encrypt data at rest and in transit.

Use AWS Lake Formation for managing data permissions and governance.

# Monitoring and Optimization #
Monitor pipelines and storage with Amazon CloudWatch.

Optimize costs using AWS Cost Explorer and S3 Intelligent-Tiering.

# Pricing #
Tool | Value
| :--- | ---: |
Lambda | 0.0000166667 USD |
