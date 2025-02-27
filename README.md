# Serif-Health Take home assessment

**Approach**

1.  **Loading the data:**
    *   Loaded both datasets into pandas DataFrames.
    *   Inspected the data to understand the schema, data types, and identify potential issues.

2.  **Cleaning the data:**
    *   **Standardize Hospital Names:** Converted hospital names to lowercase and remove spaces to ensure consistent matching.
    *   **Rename Columns:** Renamed columns to a unified schema for consistency.
    *   **Data Type Conversion:** Converted relevant columns (e.g., dates, numerical values) to the correct data types.

3.  **Merging the data:**
    *   **Identify Join Keys:** Identified (hospital name, billing code, payer name) as relavant join keys as these are the common columns in both data sets.
    *   **Perform Outer Join:** Performed a full outer join on the selected keys to ensure that all records from both datasets are included in the unified dataset.

4.  **Conflict Resolution and Data Enrichment:**
    *   **Identify Overlapping Data:** Identified cases where both datasets provide pricing information for the same service.
    *   **Calculate Discrepancies:** Calculated the difference and percentage difference between hospital charges and payer-negotiated rates.
    *   **Data Source Indicator:** Added a source column to indicate the source of each data point (hospital or payer).

5.  **Output Generation:**
    *   Created a unified dataset.
    *   Saved the unified dataset to a CSV file.
  
## Interpreting results
    * If the average 'rate_difference' is positive,we can say that on average, hospital-negotiated rates are higher than payer-negotiated rates. A negative average indicates the opposite.
    * By calculating standard deviation, we can say how varibale the differences are

## Next Steps / Improvement
    * Create a tolerance precentage for the difference in rates
    * Can use more robust statistical methods to compare prices when dealing with large datasets
    * Data Visualization - Create charts and graphs to comapre prices


## Learnings and Decisions

*   **Importance of Data Standardization:**  Standardizing hospital names and other key fields is crucial for accurate data integration.
*   **Handling Missing Data:**  The full outer join ensures that all records are included, even if some data points are missing in one of the datasets.
*   **Discrepancy Analysis:**  Calculating the differences between hospital charges and payer-negotiated rates provides valuable insights into healthcare pricing variations.




