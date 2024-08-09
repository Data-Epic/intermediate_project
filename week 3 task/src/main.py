import polars as pl
import duckdb as dd
import pyarrow

# Reading .csv file using polars
online_retail_data = pl.read_csv("New Online Retail.csv", low_memory=True)

# Ensuring there is not unneccessary duplication of data
online_retail_data = online_retail_data.unique()

# Creating a column called Total_Price
df = online_retail_data.with_columns((online_retail_data['Quantity'] * online_retail_data['UnitPrice']).alias("Total_Price").cast(pl.Float64))

# Grouping by StockCode to get the total, mean, min and max prices for each unique Stock code
finance_df = df.group_by("StockCode").agg(
    pl.sum("Total_Price").alias("Total_cost_stock_sold($)").round(2),
    pl.mean("Total_Price").alias("Average_cost_stock_sales($)").round(2),
    pl.min("Total_Price").alias("Min_sales").round(2),
    pl.max("Total_Price").alias("Max_sales").round(2)
)

# Storing file inside ratail.db as finance_data
con = dd.connect("retail.db")
#
con.register("finance_data", finance_df)
#
result = con.execute("SELECT * FROM finance_data td").pl()
print(result)



