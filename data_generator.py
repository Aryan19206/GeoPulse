
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

   vccjjk
chghchjcj
 hghvjjvhcvjvjv
hhgchj
