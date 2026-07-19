import os
os.environ["PYSPARK_PYTHON"] = r"C:\Users\HP\AppData\Local\Programs\Python\Python313\python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = r"C:\Users\HP\AppData\Local\Programs\Python\Python313\python.exe"

from pyspark.sql import SparkSession
from pyspark.sql.functions import sum

spark=SparkSession.builder.appName("Final Pipeline").getOrCreate()

data=[
    (1,100),
    (1,None),
    (2,200),
    (2,200),
    (3,None)
]

columns=["store_id","price"]

df=spark.createDataFrame(data,columns)

result=df.dropDuplicates() \
         .na.fill({"price":0}) \
         .groupBy("store_id") \
         .agg(sum("price").alias("Total_Revenue"))

result.show()

spark.stop()