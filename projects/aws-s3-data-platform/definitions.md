# Definitions #
| Type | Definition |
| :--- | :---|
| LoB | Lines Of Business. LoB owns its data and typically shares curated datastets.|
| Data Mesh | Collection of LoB's sharing curated data to create  a Data Mesh. Data Governance remains with the data owners, and enables data access for analytics and ML teams.|
| Structured Data | Data that is normalised, has a schema. Normally comes from relation database, transactional systems. Like CRM, ERP, LoB Apps. Data can be replicated from one RDBMS to others by replication logs, and or data extracts like parquet, export dmp. |
| Semi-structured Data | Data  containing identifiers but not conforming to a normalised schema. Effort needs to be used to parse the data, and may need to be joinmed with other datasets to create meaningful data.  For example sensors data in JSON,XML,YAML may contain nested levels, thesee cannot be loaded into a normalised Table without preprocessing to flatten the data. |
| Unstructured Data | Data that does not conform to a schema, is stored in individual files. Like images, vidoes, email, pdf, binary documents, etc. |
