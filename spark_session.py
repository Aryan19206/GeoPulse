
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("GeoPulse")
    .master("local[*]")
    .config("spark.driver.memory", "2g")
    .getOrCreate()
)

print("Apache Spark started successfully!")
print("Spark Version:", spark.version)

data = [
    (1001, 27.1767, 78.0081),
    (1002, 27.1844, 78.0155),
    (1003, 27.1908, 78.0084)
]

columns = ["DeviceID", "Lat", "Long"]

df = spark.createDataFrame(data, columns)

df.show()

spark.stop()
