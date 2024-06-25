import pandas as pd
import pytz

# Create a pandas DataFrame with a 'time' column in Unix timestamps (seconds)
data = {'time': [1656144000, 1656147600, 1656151200],
        'open': [100, 102, 101],
        'high': [105, 103, 104],
        'low': [98, 100, 99],
        'close': [101, 104, 102]}
df = pd.DataFrame(data)

# Convert timestamps to datetime objects in UTC (assuming data was collected in UTC)
df['time'] = pd.to_datetime(df['time'], unit='s', utc=True)

# Print the DataFrame with UTC timestamps
print("DataFrame with UTC timestamps:")
print(df)

# Set the target time zone (e.g., Asia/Tehran)
target_tz = pytz.timezone("Asia/Tehran")

# Convert the time zone of the 'time' column to target_tz
df['time_iran'] = df['time'].dt.tz_convert(target_tz)

# Print the DataFrame with both UTC and Iran time zone columns
print("\nDataFrame with UTC and Iran timestamps:")
print(df[['time', 'time_iran']])

