from pyspark.sql import SparkSession
from pyspark.sql.functions import col

print("\n===== Creating Spark Session =====")

spark = SparkSession.builder \
    .appName("Week6 Spark Assignment") \
    .getOrCreate()

print("Spark Version:", spark.version)

print("\n===== Reading CSV File =====")

df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .option("multiLine", "true") \
    .option("quote", '"') \
    .option("escape", '"') \
    .csv("Sample - Superstore.csv")

print("\n===== Displaying Dataset =====")

df.show(5)

print("\n===== Dataset Schema =====")

df.printSchema()

print("\n===== Counting Rows =====")

print("Total Rows:", df.count())

print("\n===== Saving CSV as Parquet =====")

df.write.mode("overwrite").parquet("SuperstoreParquet")

print("\n===== Reading Parquet File =====")

parquet_df = spark.read.parquet("SuperstoreParquet")

parquet_df.show(5)

print("\n===== Selecting Required Columns =====")

df.select(
    "Product ID",
    "Category",
    "Sales"
).show(5)

print("\n===== Filtering Technology Category =====")

technology_df = df.filter(
    col("Category") == "Technology"
)

technology_df.show(5)

print("\n===== Renaming Sales to Price =====")

df = df.withColumnRenamed("Sales", "Price")

df.printSchema()

print("\n===== Casting Discount to Integer =====")

df = df.withColumn(
    "Discount",
    col("Discount").cast("int")
)
df.printSchema()

print("\n===== Adding Final Price Column =====")

df = df.withColumn(
    "Final_Price",
    col("Price") * 1.18
)

df.select(
    "Product ID",
    "Price",
    "Final_Price"
).show(5)

print("\n===== Handling Null Values =====")

df.filter(
    col("Customer ID").isNull()
).show()

clean_df = df.na.drop()

print("Rows after removing null values:", clean_df.count())

print("\n===== Transformations and Actions =====")

filtered_df = clean_df.filter(
    col("Category") == "Technology"
)

selected_df = filtered_df.select(
    "Product ID",
    "Price"
)

selected_df.show()

print("\n===== Wide Transformation (Shuffle) =====")

clean_df.groupBy("Category").count().show()

print("\n===== Predicate Pushdown on Parquet =====")

parquet_df = spark.read.parquet("SuperstoreParquet")

parquet_df.filter(
    col("Category") == "Technology"
).show(5)

print("\n===== Data Pipeline (Read → Transform → Filter → Write) =====")

pipeline_df = clean_df \
    .filter(col("Category") == "Technology") \
    .select(
        "Product ID",
        "Category",
        "Price",
        "Final_Price"
    )

pipeline_df.show(5)

print("\n===== Saving Output as CSV =====")

pipeline_df.write \
    .mode("overwrite") \
    .option("header", True) \
    .csv("OutputCSV")

print("OutputCSV created successfully.")

print("\n===== Saving Output as Parquet =====")

pipeline_df.write \
    .mode("overwrite") \
    .parquet("OutputParquet")

print("OutputParquet created successfully.")

print("\n===== Best Practice: Using show() =====")

pipeline_df.show(5)

print("Avoid using collect() on large datasets.")

print("\n===== Stopping Spark Session =====")

spark.stop()

print("Spark Session Stopped Successfully.")


