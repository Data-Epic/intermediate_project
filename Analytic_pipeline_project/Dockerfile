# Use an official Python 3.10 runtime as a parent image
FROM python:3.9.19-alpine3.19

# Set the working directory
WORKDIR /Analytic_pipeline_project

# Install dependencies to allow downloading and unzipping DuckDB CLI
RUN apt-get update && apt-get install -y wget unzip

# Download and unzip DuckDB binary, then clean up
RUN wget https://github.com/duckdb/duckdb/releases/download/v1.0.0/duckdb_cli-linux-amd64.zip 
RUN unzip duckdb_cli-linux-amd64.zip 
RUN rm duckdb_cli-linux-amd64.zip    
RUN chmod +x ./duckdb

# Copy the requirements file into the container at /app
COPY requirements.txt /Analytic_pipeline_project

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /Analytic_pipeline_project

#unzip csv file for dataset 
RUN unzip online_retail.zip

# Run data ingestion script
RUN python d_ingestion.py

# Open DuckDB CLI automatically
CMD ["./duckdb", "retail.db"]