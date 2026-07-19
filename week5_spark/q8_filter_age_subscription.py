import os
os.environ["PYSPARK_PYTHON"] = r"C:\Users\HP\AppData\Local\Programs\Python\Python313\python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = r"C:\Users\HP\AppData\Local\Programs\Python\Python313\python.exe"

from pyspark.sql import SparkSession
from pyspark.sql.functions import min,max,mean

spark=SparkSession.builder.appName("Aggregation").getOrCreate()

data=[
    (100,),
    (200,),
    (300,),
    (400,)
]

df=spark.createDataFrame(data,["price"])

df.agg(
    min("price").alias("Minimum"),
    max("price").alias("Maximum"),
    mean("price").alias("Average")
).show()

spark.stop()