import pyspark.sql.functions as F
import pyspark.sql.types as T
from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.functions import regexp_replace
csv_path = "/Volumes/main/default/files/fe_medium_posts_raw.csv"
df = spark.read.csv(csv_path, header=True)

df = df.filter(df.link != 'null')
df = df.withColumn("author", regexp_replace("author", "\\([^()]*\\)", ""))

df.write.mode("overwrite").saveAsTable("mediumPostsTable")
