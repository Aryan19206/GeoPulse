
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



