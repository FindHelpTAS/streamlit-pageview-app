import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd
import pandas as pd
import seaborn as sns
from shapely.geometry import Point

# First graph: Total Pageviews Over Quarters in 2024
st.title("Total Pageviews and Bounce Rate Over Quarters")

# Data for pageviews
quarters = ['Q1 2024', 'Q2 2024', 'Q3 2024']  # List of quarters
pageviews = [70805, 52959, 59800]  # Pageviews data

# Calculate the median and average of the pageviews
median_pageviews = np.median(pageviews)
average_pageviews = np.mean(pageviews)

# Create the first graph
fig1, ax1 = plt.subplots(figsize=(8, 6))
ax1.plot(quarters, pageviews, marker='o', linestyle='-', color='b')
ax1.axhline(y=median_pageviews, color='r', linestyle='--', label=f'Median: {int(median_pageviews)}')
ax1.axhline(y=average_pageviews, color='g', linestyle='-', label=f'Average: {int(average_pageviews)}')
ax1.set_ylim(0, max(pageviews) + 5000)
ax1.set_title('Total Pageviews Over Quarters in 2024', fontsize=14)
ax1.set_xlabel('Quarter', fontsize=12)
ax1.set_ylabel('Total Pageviews', fontsize=12)
ax1.grid(True)
ax1.legend()

# Display the first graph using Streamlit
st.pyplot(fig1)

# Second graph: Bounce Rate Over Quarters in 2024
bounce_rates = [36.84, 26.46, 18.00]  # Bounce rates as percentages

# Calculate the median and average of the bounce rates
median_bounce_rate = np.median(bounce_rates)
average_bounce_rate = np.mean(bounce_rates)

# Create the second graph
fig2, ax2 = plt.subplots(figsize=(8, 6))
ax2.plot(quarters, bounce_rates, marker='o', linestyle='-', color='b')
ax2.axhline(y=median_bounce_rate, color='r', linestyle='--', label=f'Median: {median_bounce_rate:.2f}%')
ax2.axhline(y=average_bounce_rate, color='g', linestyle='-', label=f'Average: {average_bounce_rate:.2f}%')
ax2.set_ylim(0, max(bounce_rates) + 10)
ax2.set_title('Bounce Rate Over Quarters in 2024', fontsize=14)
ax2.set_xlabel('Quarter', fontsize=12)
ax2.set_ylabel('Bounce Rate (%)', fontsize=12)
ax2.grid(True)
ax2.legend()

# Display the second graph using Streamlit
st.pyplot(fig2)

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from shapely.geometry import Point
import streamlit as st

# Function to download and load the Natural Earth dataset
@st.cache_data
def load_natural_earth_data():
    url = "https://naturalearth.s3.amazonaws.com/110m_cultural/ne_110m_admin_0_countries.zip"
    world = gpd.read_file(url)
    return world

# Load the Natural Earth data (Australia map)
world = load_natural_earth_data()

# Filter for Australia (Tasmania included)
australia = world[world.SOVEREIGNT == "Australia"]

# Full dataset with Latitude, Longitude, and Sessions
data = [
    (-40.7606, 145.2955, 1.00154),
    (-40.8459, 145.1250, 1.00154),
    (-40.9897, 145.7262, 1.00540),
    (-41.0558, 145.9038, 1.01465),
    (-41.1056, 146.8261, 1.00309),
    (-41.1226, 146.0732, 1.00077),
    (-41.1480, 145.8330, 1.00000),
    (-41.1578, 147.5173, 1.00540),
    (-41.1603, 146.1824, 1.00231),
    (-41.1750, 146.3188, 1.00000),
    (-41.1769, 146.3515, 1.11415),
    (-41.1879, 146.3866, 1.00231),
    (-41.2352, 146.3511, 1.00077),
    (-41.2464, 146.4246, 1.00309),
    (-41.3203, 148.2389, 1.00077),
    (-41.3960, 147.1319, 1.00463),
    (-41.3995, 146.3390, 1.00154),
    (-41.4167, 146.9333, 1.00000),
    (-41.4388, 147.1347, 2.17079),
    (-41.4388, 147.1347, 1.00000),
    (-41.4388, 147.1347, 1.00000),
    (-41.4388, 147.1347, 1.00154),
    (-41.4388, 147.1347, 1.00000),
    (-41.4560, 148.2610, 1.00000),
    (-41.4713, 147.1595, 1.00077),
    (-41.5006, 147.0736, 1.00077),
    (-41.5159, 145.2148, 1.00000),
    (-41.5248, 146.6570, 1.00154),
    (-41.5291, 146.8391, 1.00077),
    (-41.5723, 147.1710, 1.00000),
    (-41.6051, 147.1189, 1.00309),
    (-41.6164, 146.4238, 1.00154),
    (-41.8743, 148.3024, 1.00000),
    (-42.1228, 148.0743, 1.00000),
    (-42.6648, 147.4232, 1.00154),
    (-42.7500, 147.0667, 1.00000),
    (-42.7667, 147.2500, 1.00000),
    (-42.7826, 147.0587, 1.00463),
    (-42.8125, 147.3547, 1.00000),
    (-42.8288, 147.2730, 1.01234),
    (-42.8425, 147.2959, 1.06324),
    (-42.8472, 147.3563, 1.00231),
    (-42.8509, 147.3039, 1.01465),
    (-42.8586, 147.5053, 1.00077),
    (-42.8620, 147.6552, 1.00077),
    (-42.8741, 147.3160, 1.00154),
    (-42.8755, 147.3703, 1.00154),
    (-42.8794, 147.3294, 10.00000),
    (-42.8794, 147.3294, 1.00231),
    (-42.8794, 147.3294, 1.00848),
    (-42.8794, 147.3294, 1.00154),
    (-42.8794, 147.3294, 1.00617),
    (-42.8794, 147.3294, 1.00463),
    (-42.8794, 147.3294, 1.00077),
    (-42.8794, 147.3294, 1.00154),
    (-42.8794, 147.3294, 1.00154),
    (-42.8794, 147.3294, 1.00077),
    (-42.8794, 147.3294, 1.00463),
    (-42.8794, 147.3294, 1.00000),
    (-42.8794, 147.3294, 1.00154),
    (-42.8794, 147.3294, 1.00154),
    (-42.8794, 147.3294, 1.00077),
    (-42.8933, 147.3170, 1.00077),
    (-42.8945, 147.3244, 1.00000),
    (-42.8962, 147.4453, 1.00077),
    (-42.9073, 147.4938, 1.00077),
    (-42.9333, 147.5000, 1.00077),
    (-42.9567, 147.3407, 1.00077),
    (-42.9578, 147.5315, 1.00000),
    (-42.9764, 147.3035, 1.00309),
    (-43.0017, 147.3189, 1.00000),
    (-43.0281, 147.2626, 1.00231),
    (-43.0312, 147.0481, 1.00077),
    (-43.0971, 147.7433, 1.02082),
    (-43.1323, 146.9763, 1.00000),
    (-43.1458, 147.8437, 1.01543),
    (-43.45, 169.8833, 1.00000),
    (-40.7895, -74.0565, 1.00000)
]

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data, columns=['Latitude', 'Longitude', 'Sessions'])

# Create a GeoDataFrame
geometry = [Point(xy) for xy in zip(df['Longitude'], df['Latitude'])]
gdf = gpd.GeoDataFrame(df, geometry=geometry)

# Plot Tasmania with the heatmap-like effect
fig3, ax = plt.subplots(figsize=(10, 10))

# Plot Australia for context
australia.plot(ax=ax, color='lightgrey')

# Create a heatmap using Seaborn on the latitude and longitude points
sns.kdeplot(df['Longitude'], df['Latitude'], cmap="Blues", shade=True, bw_adjust=0.5, ax=ax)

# Plot the points with their intensities
gdf.plot(ax=ax, markersize=gdf['Sessions'] * 50, color='red', alpha=0.5)

# Set title and labels
plt.title("Tasmania Heatmap Based on Sessions")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

# Display the Tasmania heatmap using Streamlit
st.pyplot(fig3)
