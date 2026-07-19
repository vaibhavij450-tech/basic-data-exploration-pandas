import os

os.environ["PYSPARK_PYTHON"] = r"C:\Users\HP\AppData\Local\Programs\Python\Python313\python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = r"C:\Users\HP\AppData\Local\Programs\Python\Python313\python.exe"

from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("Week5 Spark Assignment") \
    .getOrCreate()

# Sample Data
data = [
    (1, "2024-01-01", "Alice", 500),
    (1, "2024-01-01", "Alice", 500),
    (2, "2024-01-02", "Bob", 300),
    (3, "2024-01-03", "Charlie", 700),
    (3, "2024-01-03", "Charlie", 700)
]

columns = ["user_id", "transaction_date", "name", "amount"]

df = spark.createDataFrame(data, columns)

print("Before removing duplicates")
df.show()

df_unique = df.dropDuplicates(["user_id", "transaction_date"])

print("After removing duplicates")
df_unique.show()

spark.stop()