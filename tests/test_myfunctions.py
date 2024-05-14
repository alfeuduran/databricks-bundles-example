import pytest
import pyspark
from myfunctions import *
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, FloatType, StringType

tableName    = "diamonds"
dbName       = "default"
columnName   = "clarity"
columnValue  = "SI2"

# Because this file is not a Databricks notebook, you
# must create a Spark session. Databricks notebooks
# create a Spark session for you by default.
spark = SparkSession.builder \
                    .appName('integrity-tests') \
                    .getOrCreate()

# Create fake data for the unit tests to run against.
# In general, it is a best practice to not run unit tests
# against functions that work with data in production.
schema = StructType([ \
  StructField("_c0",     IntegerType(), True), \
  StructField("carat",   FloatType(),   True), \
  StructField("cut",     StringType(),  True), \
  StructField("color",   StringType(),  True), \
  StructField("clarity", StringType(),  True), \
  StructField("depth",   FloatType(),   True), \
  StructField("table",   IntegerType(), True), \
  StructField("price",   IntegerType(), True), \
  StructField("x",       FloatType(),   True), \
  StructField("y",       FloatType(),   True), \
  StructField("z",       FloatType(),   True), \
])

data = [ (1, 0.23, "Ideal",   "E", "SI2", 61.5, 55, 326, 3.95, 3.98, 2.43 ), \
         (2, 0.21, "Premium", "E", "SI1", 59.8, 61, 326, 3.89, 3.84, 2.31 ) ]

df = spark.createDataFrame(data, schema)

# Does the table exist?
def test_tableExists():
  assert tableExists(tableName, dbName) is True

# Does the column exist?
def test_columnExists():
  assert columnExists(df, columnName) is True

# Is there at least one row for the value in the specified column?
def test_numRowsInColumnForValue():
  assert numRowsInColumnForValue(df, columnName, columnValue) > 0