import pandas as pd

# Assuming 'data' is your original dataframe
# If you're loading from a CSV file, you can use pd.read_csv('your_file.csv')
# Replace 'your_file.csv' with the actual file path if needed

# Sample data (replace this with your actual data)
# data = {
#     'Time': ['00:00:00', '00:15:00', '01:00:00', '01:15:00', '02:00:00', '02:15:00'],
#     'Node': [10, 10, 10, 10, 10, 10],
#     'CarCount': [31, 49, 57, 44, 51, 34],
#     'BikeCount': [0, 0, 6, 0, 0, 0],
#     'BusCount': [4, 3, 15, 5, 9, 4],
#     'TruckCount': [4, 3, 16, 4, 7, 7],
#     'TrafficSituation': ['low', 'low', 'normal', 'low', 'low', 'low']
# }
data=pd.read_csv('Traffic - Copy.csv')

df = pd.DataFrame(data)

# Convert 'Time' column to datetime format
df['Time'] = pd.to_datetime(df['Time'])

# Group by hour and aggregate data
df_hourly = df.groupby(df['Time'].dt.hour).agg({
    'Node': 'first',
    'CarCount': 'sum',
    'BikeCount': 'sum',
    'BusCount': 'sum',
    'TruckCount': 'sum',
    'TrafficSituation': 'first'
}).reset_index()

# Display the new hourly dataset
print(df_hourly)
