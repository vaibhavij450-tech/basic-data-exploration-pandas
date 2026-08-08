## Theory Questions

### Q1. What are the key limitations of traditional MapReduce that make Spark a preferred choice for modern big data processing?

**Answer:**
- MapReduce stores intermediate results on disk, making it slower.
- It requires multiple jobs for complex tasks.
- It is not suitable for iterative machine learning algorithms.
- It has higher disk I/O overhead.
- Spark uses in-memory processing, making it much faster.

---

### Q2. Explain how Spark uses In-Memory Computing to speed up iterative machine learning algorithms compared to disk-based systems.

**Answer:**
Spark stores data in RAM instead of repeatedly reading and writing to disk. Since machine learning algorithms process the same data multiple times, keeping the data in memory reduces disk I/O and improves execution speed significantly.

---

### Q7. How does the immutability of Spark DataFrames affect how you perform "data cleaning" steps like dropping columns or renaming them?

**Answer:**
Spark DataFrames are immutable, meaning they cannot be modified directly. Every data cleaning operation creates a new DataFrame instead of changing the original one.

**Example:**

```python
df_new = df.drop("age")
df_new = df_new.withColumnRenamed("name", "customer_name")
```

---

### Q9. When cleaning a dataset, why is it often better to handle null values before performing mathematical aggregations like `sum()` or `avg()`?

**Answer:**
Handling null values before performing mathematical operations ensures accurate results. Null values may lead to incorrect calculations or missing values in the output. Filling or removing null values improves data quality before aggregation.

---

### Q10. Write the code to revise a column named `raw_timestamp` by casting it to a `TimestampType` and renaming it to `event_time`.

```python
from pyspark.sql.functions import col
from pyspark.sql.types import TimestampType

df = df.withColumn(
    "raw_timestamp",
    col("raw_timestamp").cast(TimestampType())
).withColumnRenamed(
    "raw_timestamp",
    "event_time"
)
```

---

### Q11. Explain the "Shuffle" process that occurs during a grouping operation. Why is it considered a wide transformation?

**Answer:**
A shuffle is the process of redistributing data across different partitions so that records with the same key are grouped together. Operations such as `groupBy()` and `join()` require shuffling. It is considered a **wide transformation** because data is transferred across multiple partitions or machines, making it more expensive than narrow transformations.

---

### Q12. Write a code snippet that identifies and removes rows where the `email` column contains null values OR the `username` is an empty string.

```python
from pyspark.sql.functions import col

df_clean = df.filter(
    col("email").isNotNull() &
    (col("username") != "")
)
```

---

### Q14. In the context of cleaning a dataset, what is the risk of using `inferSchema=true` when your source data contains messy or inconsistent date formats?

**Answer:**
When the source data contains inconsistent or invalid date formats, `inferSchema=true` may infer the wrong data type or treat dates as strings. This can lead to incorrect parsing, null values, or errors during data processing. Defining the schema manually is often a safer approach for inconsistent datasets.

---