import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("traffic.csv")

# Display info
print("Dataset Info:")
print(df.info())
print("\nFirst 5 Rows:")
print(df.head())

# Convert date column
df['date'] = pd.to_datetime(df['date'])

# Total Clicks Over Time
clicks_per_day = df.groupby('date').size()

plt.figure(figsize=(14, 6))
clicks_per_day.plot(kind='line', marker='o')
plt.title("Total Clicks Over Time")
plt.xlabel("Date")
plt.ylabel("Number of Clicks")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("total_clicks_over_time.png")  
plt.show()

# Top 10 Countries by Clicks
top_countries = df['country'].value_counts().head(10)

plt.figure(figsize=(10, 6))
top_countries.plot(kind='bar', color='skyblue')
plt.title("Top 10 Countries by Clicks")
plt.xlabel("Country")
plt.ylabel("Number of Clicks")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.savefig("top_countries_by_clicks.png")  
plt.show()

# Top 10 Cities by Clicks
top_cities = df['city'].value_counts().head(10)

plt.figure(figsize=(10, 6))
top_cities.plot(kind='bar', color='lightgreen')
plt.title("Top 10 Cities by Clicks")
plt.xlabel("City")
plt.ylabel("Number of Clicks")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.savefig("top_cities_by_clicks.png") 
plt.show()

# Top 10 Artists by Clicks
top_artists = df['artist'].value_counts().head(10)

plt.figure(figsize=(10, 6))
top_artists.plot(kind='bar', color='salmon')
plt.title("Top 10 Artists by Clicks")
plt.xlabel("Artist")
plt.ylabel("Number of Clicks")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.savefig("top_artists_by_clicks.png")  
plt.show()

# Top 10 Tracks by Clicks
top_tracks = df['track'].value_counts().head(10)

plt.figure(figsize=(10, 6))
top_tracks.plot(kind='bar', color='orange')
plt.title("Top 10 Tracks by Clicks")
plt.xlabel("Track")
plt.ylabel("Number of Clicks")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.savefig("top_tracks_by_clicks.png")  
plt.show()
