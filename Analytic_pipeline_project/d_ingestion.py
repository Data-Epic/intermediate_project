import polars as pl
import duckdb

df = pl.read_csv('online_retail(cleaned).csv')

# Add 'TotalAmount' column
df = df.with_columns((pl.col('Quantity') * pl.col('UnitPrice')).round(2).alias('Total_Amount'))

#Create new columns for finance adata
finance_df = df.group_by("StockCode").agg(
    pl.sum("Total_Amount").alias("Total_cost_stock_sold").round(2),
    pl.mean("Total_Amount").alias("Average_cost_stock_sales").round(2),
    pl.min("Quantity").alias("Min_sales"),
    pl.max("Quantity").alias("Max_sales")
    )
# Store the finance data in the database
finance_df.write_database(
    table_name='finance_data',
    connection="duckdb:///finance.db",
    if_table_exists='replace'
)

print('data saved to database successfully')

# test the connection
#with duckdb.connect(database="retail.db", read_only=False) as con:
#    con.query("SELECT * FROM finance_data").show()