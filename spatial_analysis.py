
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from pathlib import Path


def create_spatial_data(df):

    geometry = [
        Point(longitude, latitude)
        for longitude, latitude in zip(df["Long"], df["Lat"])
    ]

    spatial_df = gpd.GeoDataFrame(
        df.copy(),
        geometry=geometry,
        crs="EPSG:4326"
    )

    return spatial_df


if __name__ == "__main__":

    base_path = Path(__file__).resolve().parent.parent

    input_file = base_path / "data" / "processed" / "cleaned_gps_data.csv"

    output_file = (
        base_path / "data" / "processed" / "spatial_gps_data.geojson"
    )

    gps_df = pd.read_csv(input_file)

    spatial_df = create_spatial_data(gps_df)

    spatial_df.to_file(output_file, driver="GeoJSON")

    print("Spatial processing completed!")
    print("Total GPS points:", len(spatial_df))
    print("Coordinate system:", spatial_df.crs)
    print("Saved to:", output_file)
