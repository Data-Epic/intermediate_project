# Week 2 Task: Wrangling Online Retail Data

## Data cleaning steps documentation

### **1. Library Importation**
To begin the data cleaning process, all the necessary libraries were imported. In this task, we used fetch_ucirepo, pandas, numpy, matplotlib and seaborn.

1. **`fetch_ucirepo`**: To extract the datasets from the UC Irvine Machine Learning Repository. It provided a more convenient way to access and load the Online Retail dataset.
2. **`pandas`**: It is used for the data manipulation, including loading, merging, cleaning, and transforming data.
3. **`numpy`**: It is used for numerical operations.
4. **`matplotlib.pyplot`**: It was used to used for generating visualizations.
5. **`seaborn`**: It was used to used for generating visualizations.

Each libraries were chosen to fulfill specific roles in data handling, visualization, and analysis, making the cleaning process more efficient and effective.

### **2. Data Loading**
Loaded the [Online Retail](http://archive.ics.uci.edu/dataset/352/online+retail) dataset from the UC Irvine Machine Learning Repository using the `fetch_ucirepo` library to perform data cleaning on the Online Retail dataset.

### **3. Data Inspection**
1. **Dataset Information**: To provides an overview of the datasets including column names, data types, and the count of non-null values.
2. **Shape of the Dataset**: To provides the number of rows and columns in the dataframe.
3. **Statistical Summary**: To generates descriptive statistics for numerical columns (e.g., count, mean, standard deviation, min, max).
4. **Missing Values**: To provide the number of missing values in each column.
5. **Duplicate Rows**: To provides the counts of the number of duplicate rows in the dataframe.
6. **Unique Values per Column**: To shows the number of unique values in each column.
7. **Zero Values per Column**: To provides the counts of the number of zero values in each column.

### **4. Handling Missing Values**
The missing values in 'Description' were replaced with 'No Description' to maintain the context while the missing values in 'CustomerID' were set to `-1` to indicate missing customer identifiers without losing data rows.

### **5. Handling Duplicates**
Duplicates data can distort what we want to use the data for and were removed to ensure data integrity.

### **6. Inconsistent Formatting**
The text data in 'Description' and 'Country' columns were normalize to ensure consistency in text data by fixing the formatting inconsistencies in 'Decription' column and Standardizing the 'Country' column by replacing specific country codes with their full names.

### **7. Incorrect Data Types**
Convert 'InvoiceDate' to a proper datetime format to ensure correct data type.

### **8. Handling Outliers**
The methos involved both Interquartile Range method (IQR method) and visual (box plot) techniques to detect outliers in the 'Quantity' and 'UnitPrice' columns. However, due to the severity or nature of outliers observed in the data, manual thresholding was employed after visual inspection to ensure that only relevant data points were retained. 

### **9. Data Validation**
The cleaned data were validated that the cleaned data adheres to expected ranges and contains no unexpected or reintroduced issues by ensuring it meets the specified requirements before saving or used.

### **10. Final Data Output**
Saved the cleaned dataset to a CSV file to preserve the cleaned data. 