
from sedona.spark import SedonaContext

config = (
    SedonaContext.builder()
    .appName("GeoPulse-Sedona")
    .master("local[*]")
    .config(
        "spark.jars.packages",
        "org.apache.sedona:sedona-spark-3.5_2.12:1.7.1"
    )
    .getOrCreate()
)

sedona = SedonaContext.create(config)

print("Apache Sedona started successfully!")
print("Spark Version:", sedona.version)

sedona.sql("""
    SELECT ST_AsText(ST_Point(78.0081, 27.1767)) AS location
""").show(truncate=False)

sedona.stop()
