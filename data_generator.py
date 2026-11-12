
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime, timedelta


def generate_gps_data(num_records=100000):
    np.random.seed(42)

    device_ids = np.random.randint(1001, 5001, num_records)

    latitude = np.random.normal(27.1767, 0.015, num_records)
    longitude = np.random.normal(78.0081, 0.015, num_records)

    start_time = datetime.now()

    timestamps = [
        start_time + timedelta(minutes=int(i * 2))
        for i in range(num_records)
    ]

    data = pd.DataFrame({
        "DeviceID": device_ids,
        "Lat": latitude,
        "Long": longitude,
        "Timestamp": timestamps
    })

    return data


if __name__ == "__main__":
    base_path = Path(__file__).resolve().parent.parent

    output_file = base_path / "data" / "raw" / "gps_data.csv"

    output_file.parent.mkdir(parents=True, exist_ok=True)

    gps_df = generate_gps_data()

    gps_df.to_csv(output_file, index=False)

    print("GPS mobility dataset generated successfully!")
    print("Total GPS pings:", len(gps_df))
    print(gps_df.head())
    print("Saved to:", output_file)
