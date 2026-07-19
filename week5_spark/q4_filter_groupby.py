import os

os.environ["PYSPARK_PYTHON"] = r"C:\Users\HP\AppData\Local\Programs\Python\Python313\python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = r"C:\Users\HP\AppData\Local\Programs\Python\Python313\python.exe"

from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

# Create Spark Session
spark = SparkSession.builder \
    .appName("Week5 Spark Assignment") \
    .getOrCreate()

# Sample Sales Data
data = [
    ("West", "Electronics", 500),
    ("West", "Electronics", 700),
    ("West", "Furniture", 300),
    ("East", "Furniture", 450),
    ("West", "Furniture", 250),
    ("North", "Electronics", 800)
]

columns = ["region", "product_category", "sale_amount"]

df_sales = spark.createDataFrame(data, columns)

print("Original Data")
df_sales.show()

result = df_sales.filter(df_sales.region == "West") \
    .groupBy("product_category") \
    .agg(avg("sale_amount").alias("Average_Sale"))

print("Average Sale Amount")
result.show()

spark.stop()