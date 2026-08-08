# Azure Cloud Fundamentals and Data Pipeline Implementation using Azure Data Factory

## Objective

Build an end-to-end data pipeline using Azure Blob Storage and Azure Data Factory (ADF).

---

## Azure Services Used

- Azure Resource Group
- Azure Storage Account
- Azure Blob Storage
- Azure Data Factory
- Azure Blob Linked Service
- Copy Data Activity

---

## Project Workflow

1. Created a Resource Group.
2. Created an Azure Storage Account.
3. Created a Blob Container.
4. Uploaded the Sample Superstore CSV dataset.
5. Created Azure Data Factory.
6. Configured Linked Service for Blob Storage.
7. Created Source Dataset.
8. Created Destination Dataset.
9. Built a Copy Data Pipeline.
10. Published the pipeline.
11. Executed the pipeline successfully.
12. Verified output.csv in Blob Storage.

---

## Architecture

```
Sample - Superstore.csv
        │
        ▼
Azure Blob Storage
        │
        ▼
Azure Data Factory
(Copy Data Activity)
        │
        ▼
output.csv
```

---

## Result

The Azure Data Factory pipeline executed successfully and copied the source CSV file to the destination blob storage as output.csv.

---

## Screenshots

All screenshots are available in the **Screenshots** folder.
