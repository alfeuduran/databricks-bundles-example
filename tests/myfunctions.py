import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Because this file is not a Databricks notebook, you
# must create a Spark session. Databricks notebooks
# create a Spark session for you by default.
spark = SparkSession.builder \
                    .appName('integrity-tests') \
                    .getOrCreate()

# Does the specified table exist in the specified database?
def tableExists(tableName, dbName):
  return spark.catalog.tableExists(f"{dbName}.{tableName}")

# Does the specified column exist in the given DataFrame?
def columnExists(dataFrame, columnName):
  if columnName in dataFrame.columns:
    return True
  else:
    return False

# How many rows are there for the specified value in the specified column
# in the given DataFrame?
def numRowsInColumnForValue(dataFrame, columnName, columnValue):
  df = dataFrame.filter(col(columnName) == columnValue)

  return df.count()