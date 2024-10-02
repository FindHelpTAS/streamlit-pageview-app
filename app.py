import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# First graph: Total Pageviews Over Quarters in 2024
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

# Second graph: Bounce Rate Over Quarters in 2024
# Data for bounce rates
bounce_rates = [36.84, 26.46, 18.00]  # Bounce rates as percentages

# Calculate the median and average of the bounce rates
median_bounce_rate = np.median(bounce_rates)
average_bounce_rate = np.mean(bounce_rates)

# Create the second graph
fig2, ax2 = plt.subplots(figsize=(8, 6))
ax2.plot(quarters, bounce_rates, marker='o', linestyle='-', color='b')
ax2.set_ylim(0, max(bounce_rates) + 10)
ax2.set_title('Bounce Rate Over Quarters in 2024', fontsize=14)
ax2.set_xlabel('Quarter', fontsize=12)
ax2.set_ylabel('Bounce Rate (%)', fontsize=12)
ax2.grid(True)
ax2.legend()

# Display both graphs using Streamlit
st.pyplot(fig1)  # Display the first graph
st.pyplot(fig2)  # Display the second graph

import streamlit as st
import streamlit.components.v1 as components

# Embed your HTML and JavaScript code in a string
html_code = '''
<!DOCTYPE html>
<html>
<head>
    <title>Google Maps Heatmap and Markers with Reverse Geocoding</title>
    <script>
        let map, heatmap;

        // Callback function to initialize the map after the script has loaded
        function initMap() {
            map = new google.maps.Map(document.getElementById("map"), {
                zoom: 6,
                center: { lat: -41.4388, lng: 147.1347 }, // Centered on Tasmania
                mapTypeId: "terrain",
            });

            // Create and add a legend for the heatmap
            const legend = document.getElementById("legend");
            map.controls[google.maps.ControlPosition.RIGHT_BOTTOM].push(legend);

            // Fetch the CSV data (replace this with your actual file path or API)
            fetch('Cleaned_Council_Mapping.csv')
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok ' + response.statusText);
                    }
                    return response.text();
                })
                .then(csvData => {
                    const parsedData = parseCSV(csvData);
                    createHeatmap(parsedData);
                    createMarkers(parsedData);
                })
                .catch(error => console.error('Error fetching CSV data:', error));
        }

        // Parse CSV Data
        function parseCSV(csvData) {
            const rows = csvData.trim().split('\\n').slice(1); // Skip header row
            const locations = rows.map(row => {
                const [lat, lng, sessions] = row.split(',');
                return {
                    lat: parseFloat(lat),
                    lng: parseFloat(lng),
                    sessions: parseInt(sessions),
                };
            });
            return locations;
        }

        // Heatmap Layer
        function createHeatmap(locations) {
            const heatmapData = locations.map(location => ({
                location: new google.maps.LatLng(location.lat, location.lng),
                weight: location.sessions,
            }));
            heatmap = new google.maps.visualization.HeatmapLayer({
                data: heatmapData,
                radius: 70, // Adjust radius to better visualize smaller points
                opacity: 0.7,
                gradient: [
                    'rgba(239,251,16,0)',
                    'rgba(241,221,14,1)',
                    'rgba(243,194,13,1)',
                    'rgba(244,174,12,1)',
                    'rgba(245,159,11,1)',
                    'rgba(246,139,10,1)',
                    'rgba(247,124,9,1)',
                    'rgba(248,107,8,1)',
                    'rgba(249,90,7,1)',
                    'rgba(250,75,6,1)',
                    'rgba(251,55,5,1)',
                    'rgba(252,40,4,1)',
                    'rgba(253,30,4,1)',
                    'rgba(253,18,4,1)',
                    'rgba(253,13,4,1)',
                    'rgba(254,3,3,1)',
                ],
                map: map,
            });
        }
    </script>
    <style>
        #map {
            height: 500px;
            width: 100%;
        }

        #legend {
            background: white;
            padding: 10px;
            margin: 10px;
            font-family: Arial, sans-serif;
            font-size: 12px;
            font-weight: bold;
        }

        #legend .title {
            margin-bottom: 5px;
        }

        #legend .gradient {
            background: linear-gradient(to right, rgb(239, 251, 16), rgba(254, 3, 3, 1));
            height: 15px;
            width: 200px;
            margin-bottom: 5px;
        }

        #legend .scale {
            display: flex;
            justify-content: space-between;
        }
    </style>
</head>

<body>
    <div id="map"></div>

    <!-- Legend for Heatmap -->
    <div id="legend">
        <div class="title">Heatmap Intensity</div>
        <div class="gradient"></div>
        <div class="scale">
            <span>1</span>
            <span>12,000</span>
        </div>
    </div>

    <!-- Load the Google Maps JavaScript API asynchronously -->
    <script
        src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBJDGu-1xitUVcPe7Hgo412Rjik-9hO7qc&libraries=visualization&callback=initMap"
        async defer></script>
</body>
</html>
'''

# Use Streamlit to render the HTML
components.html(html_code, height=600)
