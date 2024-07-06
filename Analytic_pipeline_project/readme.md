##  An online retail Pipeline

The project utilizes an ETL (Extract, Transform, Load) pipeline for  an online-Retail data. It uses Polars for data ingestion, preprocessing, and analysis and  DuckDB as the preferred database. The entire pipeline process, data ingestion scripts and the DuckDB database, is containerized with Docker for  deployment and scalability.

Input
Primary dataset for the ETL process:Online_Retail.csv

### Output
An aggregated table with the following columns:
1. StockCode
2. Total_Stock_Sold
3. Average_Cost
4. Min_Sales
5. Max_Sales

### Requirements
1. duckdb-engine 
2. pandas 
3. pyarrow 
4. sqlalchemy  
