## Read Dataset
      import pandas as pd
      
      # can accept URL or file path
      df = pd.read_csv("...")
      
## Attribute of DataFrame
      # return (num_rows, num_columns)
      df.shape()
      
      # return first 5 rows by default
      df.head()
      df.head(10) # first 10 rows
      
      # return last 5 rows by default
      df.tail()
      df.tail(10) # last 10 rows
      
      # return datatype of all columns in a DataFrame
      df.dtypes
      
      # return summary of dataframe (num of rows& column, columns name, number of non-null elements and dtype)
      df.info()
      
## Selecting & Assiging
      # Index Based Selection, iloc
      df.iloc[ 0, 9]  # 0 rows, 9 columns (0-8th column)
      
      df.iloc[0:5, 0:9] # 0-4th rows, 0-8th columns
      
      # Label Based Selection, loc
      df.loc[0:5, ["col2", "col3"] ]  # 0-5th columns, columns with column name "col2" and "col3"
      
## Selecting Columns
      df.colA
      df["colA"]
      df[ ["colA", "colB", "colC"] ]
      df[ df.colA == "None" ]   # select rows whic satisfy the condition
      
## Summary Functions
      df.describe() # different summary will be shown for numerical columns and categorical columns
      df.describe( include="all" )  # combine summary of numerical and categorical
      df.colA.describe()
      df["colA"].describe()

  - count: Number of non-null values 
  - unique: Number of unique values (cat. only)
  - top: Value of max number of occurences (cat. only)
  - freq: Number of times top appears (cat. only)
  - mean
  - std
  - min
  - 25%
  - 50%
  - 75%
  - max: Maximum Value
  - NaN values: Not available

## Aggregate Functions

        df.colA.mean()
        df.colA.unique()
        df.colA.value_counts()  # number of times every unique value occurs
        
## Sorting
        df_sorted = df.sort_values( by = "colA" )
        df.sort_values( by = "colA", ascending = False) # sort in descending order
        
## Renaming
        # columns
        df.rename(columns = { "column A":"colA", "column B":"colB" }, inplace = True)
        
        # rows
        df.rename(index = { 0:"zero", 1:"one" }.  inplace = True)
        
 ## Missing Data
        # return a dataframe with true/false only that indicates whether they are null values
        df.isnull()
        df.isna()
        
        # get number of occurences of null values
        df.isnull().sum()
        df.isna().sum()
        
        # filling the null values with some other values
        df.fillna("unknown", inplace = True)
        df.colA.fillna("Unknown", inplace = True)
