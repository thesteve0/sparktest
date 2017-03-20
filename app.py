import sys

from pyspark.sql import SparkSession


dbhost = os.env.get('MASTER_PORT_5432_TCP_ADDR')
dbport = '5432'
username = 'postgres'
password = 'password'
table = 'public.marineobs'
db = 'MOLW'

jdbcDF = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://" + dbhost + "/" + db) \
    .option("dbtable", table) \
    .option("user", username) \
    .option("password", password) \
    .option("driver", "org.postgresql.Driver") \
    .load()

print(jbcDF2.show())