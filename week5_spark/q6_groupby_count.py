import os
os.environ["PYSPARK_PYTHON"] = r"C:\Users\HP\AppData\Local\Programs\Python\Python313\python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = r"C:\Users\HP\AppData\Local\Programs\Python\Python313\python.exe"

from pyspark.sql import SparkSession
from pyspark.sql.functions import count

spark = SparkSession.builder.appName("GroupBy Count").getOrCreate()

data = [
    ("Delhi",),
    ("Delhi",),
    ("Delhi",),
    ("Mumbai",),
    ("Mumbai",),
    ("Chennai",)
]

df = spark.createDataFrame(data, ["city"])

result = df.groupBy("city") \
           .agg(count("*").alias("Total")) \
           .filter("Total > 2")

result.show()

spark.stop()