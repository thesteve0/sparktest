#Simple Example Connecting Spark to a DB (Python)

## To do an S2I build, the Oshinko builder requires more information 

    oc new-app --template=oshinko-pyspark-build-dc \
          -p APPLICATION_NAME=dbtest \
          -p GIT_URI=https://github.com/thesteve0/sparktest \
          -p APP_ARGS=--servers=apache-kafka:9092 \
          -p SPARK_OPTIONS='--packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.1.0'