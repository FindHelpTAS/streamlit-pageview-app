import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Update these lists with your new data
quarters = ['Q1 2024', 'Q2 2024', 'Q3 2024']  # Add new quarters here
pageviews = [70805, 52959, 59800]  # Add new pageviews data here

# Calculate the median and average of the pageviews
median_pageviews = np.median(pageviews)
average_pageviews = np.mean(pageviews)

# Create the graph with Y-axis starting at 0
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(quarters, pageviews, marker='o', linestyle='-', color='b')

# Plot the median as a red dotted line
ax.axhline(y=median_pageviews, color='r', linestyle='--', label=f'Median: {int(median_pageviews)}')

# Plot the average as a green line
ax.axhline(y=average_pageviews, color='g', linestyle='-', label=f'Average: {int(average_pageviews)}')

# Set the Y-axis limits to start from 0 and go to a little above the max value
ax.set_ylim(0, max(pageviews) + 5000)

# Add titles and labels
ax.set_title('Total Pageviews Over Quarters in 2024', fontsize=14)
ax.set_xlabel('Quarter', fontsize=12)
ax.set_ylabel('Total Pageviews', fontsize=12)
ax.grid(True)

# Add legend
ax.legend()

# Display the graph using Streamlit
st.pyplot(fig)
