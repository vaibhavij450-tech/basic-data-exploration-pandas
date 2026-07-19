import os
os.environ["PYSPARK_PYTHON"] = r"C:\Users\HP\AppData\Local\Programs\Python\Python313\python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = r"C:\Users\HP\AppData\Local\Programs\Python\Python313\python.exe"

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Null Handling").getOrCreate()

data = [
    (1, "Active"),
    (2, None),
    (3, "Inactive"),
    (4, None)
]

columns = ["id", "status"]

df = spark.createDataFrame(data, columns)

print("Original Data")
df.show()

print("After Filling Nulls")
df.na.fill({"status": "Unknown"}).show()

spark.stop()