#Data Ingestion
import polars as pl
import re

# Loading  excel file using Polars
file = './Online Retail.xlsx' 
df = pl.read_excel(source=file, infer_schema_length=10000)

# Drop rows with missing 'Description'
df = df.drop_nulls(subset=['Description'])

# Filling the  missing 'CustomerID' with '00000'
df = df.with_columns(pl.col('CustomerID').fill_null('00000'))

# Filtering the   InvoiceNo rows that  matches the  - d{5} or C d{5} pattern
df = df.filter(pl.col('InvoiceNo').cast(pl.Utf8).str.contains(r'^(C)?\d{6}$'))

# Extract 5 digit numbers from StockCode and drop rows with missing StockCode
df = df.with_columns(pl.col('StockCode').str.extract(r'(\d{5})', 1).alias('StockCode')).drop_nulls(subset=['StockCode'])

# Remove rows where Description contains only digits
df = df.filter(~pl.col('Description').apply(lambda x: x.isdigit(), return_dtype=pl.Boolean))

#remove leading/trailing whitespaces and standardize to lowercase,
df = df.with_columns(pl.col('Description').str.strip_chars().str.to_lowercase()) 

# Remove special characters from Description
df = df.with_columns(pl.col('Description').apply(lambda x: re.sub(r'[^\w\s]', '', x), return_dtype=pl.Utf8))
 
#convert country names to title case
df =  df.with_columns(pl.col('Country').str.to_titlecase())

#Remove rows where Quantity and UnitPrice are equal to or less than 0
df = df.filter(pl.col('Quantity') > 0).filter(pl.col('UnitPrice') > 0)

# Convert all rows to the respective data types
df = df.with_columns(
    pl.col('InvoiceNo').cast(pl.Utf8),
    pl.col('StockCode').cast(pl.Utf8),
    pl.col('Description').cast(pl.Utf8),
    pl.col('Quantity').cast(pl.Int64),
    pl.col("InvoiceDate").str.to_datetime(format="%m/%d/%y %H:%M"),
    pl.col('UnitPrice').cast(pl.Float64),
    pl.col('CustomerID').cast(pl.Utf8),
    pl.col('Country').cast(pl.Utf8)
)

# Remove duplicate rows
df = df.unique()

# Add 'TotalAmount' column
df = df.with_columns((pl.col('Quantity') * pl.col('UnitPrice')).round(2).alias('TotalAmount'))

# Save the cleaned data to a CSV file
df.write_csv('online_retail(cleaned).csv')
print('Data cleaned and saved to online_retail.csv')