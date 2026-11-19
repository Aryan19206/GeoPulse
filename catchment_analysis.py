

from sedona.spark import SedonaContext

spark = (
    SedonaContext.builder()
    .appName("GeoPulse-Catchment-Analysis")
    .master("local[*]")
    .config(
        "spark.jars.packages",
        "org.apache.sedona:sedona-spark-3.5_2.12:1.7.1"
    )
    .getOrCreate()
)

sedona = SedonaContext.create(spark)

# Load store locations
stores = sedona.read.option("header", "true").csv(
    "data/stores/store_locations.csv"
)

stores.createOrReplaceTempView("stores")

# Generate accurate 500-metre catchment areas
catchments = sedona.sql("""
    SELECT
        StoreID,
        StoreName,
        ST_Buffer(
            ST_SetSRID(
                ST_Point(
                    CAST(Long AS DOUBLE),
                    CAST(Lat AS DOUBLE)
                ),
                4326
            ),
            500,
            true
        ) AS catchment_area
    FROM stores
""")

catchments.createOrReplaceTempView("catchments")

# Display a concise validation report
sedona.sql("""
    SELECT
        StoreID,
        StoreName,
        ST_GeometryType(catchment_area) AS geometry_type,
        ST_IsValid(catchment_area) AS is_valid,
        ST_SRID(catchment_area) AS srid
    FROM catchments
""").show(truncate=False)

print("500-metre catchment analysis completed!")

sedona.stop()
