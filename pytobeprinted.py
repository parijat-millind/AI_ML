import pandas as pd

db=pd.read_csv('Traffic - Copy.csv')
df=pd.DataFrame(db)

#drop duplicates
df=df.drop_duplicates(subset=['Time'], keep='first')  

# Assuming df is your DataFrame
df = df.dropna()

# Assuming df is your DataFrame and 'Time' is your time column
df['Time'] = pd.to_datetime(df['Time'])

# Filter out rows where the minutes part is not zero
df = df[df['Time'].dt.minute == 0]

# Convert 'Time' back to string and remove the date part
df['Time'] = df['Time'].dt.time.astype(str)

df.to_csv('TrafficCopy21.csv', index=False)