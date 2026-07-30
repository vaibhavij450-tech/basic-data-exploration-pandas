# Week 7 - Delta Lake Incremental Processing

## Objective
Perform incremental data processing using Delta Lake.

## Steps Performed
1. Loaded customer data into a Delta table.
2. Removed duplicate records.
3. Replaced null values with "Unknown".
4. Created an incremental dataset.
5. Applied a MERGE operation to update existing records and insert new ones.
6. Validated the final dataset by checking row count and duplicate records.
7. Displayed the final dataset.

## Results
- Initial Records: 6
- Records after Cleaning: 5
- Final Records after MERGE: 7
- Duplicate Records: 0

## Technologies Used
- Databricks Free Edition
- Apache Spark (PySpark)
- Delta Lake

## Files Included
- delta_scd_assignment.ipynb
- README.md
- Screenshots
