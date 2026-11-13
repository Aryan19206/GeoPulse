
import pandas as pd
from pathlib import Path


def clean_gps_data(df):

    print("Starting GPS data cleaning...")

    df = df.drop_duplicates()

    df = df.dropna(
        subset=["DeviceID", "Lat", "Long", "Timestamp"]
    )

    df = df[
        df["Lat"].between(-90, 90)
        & df["Long"].between(-180, 180)
    ]

    df["Timestamp"] = pd.to_datetime(
        df["Timestamp"], errors="coerce"
    )

    df = df.dropna(subset=["Timestamp"])

    return df


if __name__ == "__main__":

    base_path = Path(__file__).resolve().parent.parent

    input_file = base_path / "data" / "raw" / "gps_data.csv"
    output_file = base_path / "data" / "processed" / "cleaned_gps_data.csv"

    gps_df = pd.read_csv(input_file)

    cleaned_df = clean_gps_data(gps_df)

    output_file.parent.mkdir(parents=True, exist_ok=True)

    cleaned_df.to_csv(output_file, index=False)

    print("\nGPS cleaning completed!")
    print("Original records:", len(gps_df))
    print("Cleaned records:", len(cleaned_df))
    print("Removed records:", len(gps_df) - len(cleaned_df))
    print("Saved to:", output_file)
