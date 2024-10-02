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
import streamlit as st

# Function to download and load the Natural Earth dataset
@st.cache_data
def load_natural_earth_data():
    url = "https://naturalearth.s3.amazonaws.com/110m_cultural/ne_110m_admin_0_countries.zip"
    world = gpd.read_file(url)
    return world

# Load the Natural Earth data (Australia map)
world = load_natural_earth_data()

# Check the available columns in the GeoDataFrame
st.write(world.columns)
st.write(world.head())