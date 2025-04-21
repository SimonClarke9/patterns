# Data Platform Using AWS #

## Summary ##
Use AWS Cloud to build a Data Platform. In this Data Platform we want to manage structured data, semi-structured data, and Unstructured data.
I have split this project into:
- Summary
- Architecture 
- Data Governance
- Data Pipelines

### Assumptions ###
<details>
<summary>Assumptions applying to this projects.</summary>

| Question | Assumtion |
| :--- | :---|
| What data is to be ingested | Let's assume Structured data will be CSV or JSON (excluding XML for this project to keep document types as simple list). <br> Unstructured Data will be images, binary files, text files |
| How often does data need to be ingested |  For Steaming Data, assume 15 minutes latency. <br> For Batch collection, assume 1hr intervals |

</details>

## Architecture ##
<detials>
<summary>Explain  with  top level diagram the Tools to be used.</summary>

'''python
import image as architecture
'''

</details>

### Data Structure ###
#### Layered Architecture
- Raw Layer
- Processed Layer
- Curated Layer

## Data Governance ##
### Versioning ###
Implement version control for dataset (schemas) in both raw and processed layersto track change.
### Access Control ###
- AWS IAM roles and policy to enfore least-priviledge access. Implement access controls using AWS IAM and encrypt data at rest and in transit.
- Implement fine-grained access controles using AWS Lake Formention or AWS Glue Data Catalog.
- Use AWS Lake Formation for managing data permissions and governance.

### Metadata and Cataloging ###
- Use AWS Glue=for automatic schema discovery and metadata management.
- Maintain a centralised catalog to make datasets searchable and document their lineage.
### Storage ###
- Data Encryption: Apply server-side encryption (SSE) for data stored in S3 and enable in-transit encryption using TLS
- File Formats; store raw data in gziped compressed text files especially for JSON and CSV file types : Enable S3 bucket compression
- Use columnar formats like Parquet or ORC  for curated data.
- Use Partioning structures based on time, source, or data type for improved accessability
- Lifecycyle policies: Use S3 lifecycle policies to manage storage costs by archiving older data to Amazon Glacier.
### Monitoring and Optimization ###
Monitor pipelines and storage with Amazon CloudWatch.
Optimize costs using AWS Cost Explorer and S3 Intelligent-Tiering.


## Data Pipeleines ##
### Data Ingestion ###
Use AWS services like Kinesis Data Streams or AWS Glue to ingest data from sources like website clickstreams, purchase history, product catalogs, and user demographics.
- Use Event driven pipelines for streaming data: AwS Lambda AWS Kinesis
- AWS Data Pipeline or Apache Airflow for scheduling batch ingestion/
### ETL Processing ###
- Use AWS Glue or pySpark for scalable transformations.
- Implement preprocessing steps like:
    - Data Cleaning
    - Imputation
    - Feature transformation
# Data Analytics #
Use Amazon Redshift or Athena for querying and analyzing data stored in S3.
Integrate with Amazon QuickSight for visualization and reporting.
# Machine Learning Integration #
Prepare data for machine learning models using Amazon SageMaker.
Train and deploy recommendation models that leverage user behavior and product data.

### Job Orchestration ###
- Use AWS Step, or Airflow to orchestrate workflows and ensure fault tolerance.









# Pricing #
Tool | Value | Last Update |
| :--- | ---: | ---: |
| Lambda : <br> compute: RAM GB * Request seconds/month * Compute Cost<br>  Request: Num Requests * Request Cost <br> Ephemeral: Ephemeral size GB - 0.5GB * Ephemeral cost  | Compute: 0.0000166667 USD <br> Request: 0.0000002 USD <br> Ephemeral: 0.0 USD | Apr 2025 |
| AWS Glue billy hourly for streaming ETL while thy are running. | |


# Further Reading #
| References | Link URL | Age |
| :--- | :--- | ---: |
| Building Secure Data Lakes with AWS | https://community.aws/content/2mwYy9bQazyXKRJwnGtjl8feXt4/building-secure-data-lakes-with-aws-from-s3-to-ml | 15 December 2024 |
| Build and Train ML models using data mesh architecture on AWS | https://aws.amazon.com/blogs/machine-learning/part-1-build-and-train-ml-models-using-a-data-mesh-architecture-on-aws/ | 29 July 2022 |
| Building the ML Platform | https://docs.aws.amazon.com/whitepapers/latest/build-secure-enterprise-ml-platform/building-the-ml-platform.html | AWS 2025 |
| Kinesis Connections | https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-connect-kinesis-home.html | AWS 2025 |
| Read data from Kinesis Data Streams using AWS Glue | https://docs.aws.amazon.com/streams/latest/dev/using-other-services-glue.html | 