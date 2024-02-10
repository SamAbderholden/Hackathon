import csv
from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim
import folium
import os

def read_zip_coordinates(zip_code):
    with open('./static/zipToLoc.txt', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['ZIP'] == zip_code:
                return float(row['LAT']), float(row['LNG'])
    return None, None

def get_location(zip_code):
    lat, lng = read_zip_coordinates(zip_code)
    if lat is not None and lng is not None:
        return lat, lng

    try:
        geolocator = Nominatim(user_agent="Geopy Library")
        location = geolocator.geocode(zip_code, timeout=10)
        return (location.latitude, location.longitude) if location else (None, None)
    except GeocoderTimedOut:
        return get_location(zip_code)  # Retry on timeout

def create_map(urgent_care_list, userZip):
    # Get user's location based on the provided ZIP code
    lat, long = get_location(userZip)

    # Create a folium map centered at the user's location
    m = folium.Map(location=[lat, long], zoom_start=12)

    # Use a default value if urgent_care_list is empty
    urgent_care_list = urgent_care_list or [1]

    for urgent_care in urgent_care_list:
        # Replace these with data from scraping
        name = urgent_care['fullName']
        address = f"{urgent_care['address']['line1']}, {urgent_care['address']['city']}, {urgent_care['address']['state']}, {urgent_care['address']['zip']}"
        phone = urgent_care["phone"]

        # Get location based on urgent care address
        getLoc = Nominatim(user_agent="Geopy Library").geocode(address)
        lat, long = getLoc.latitude, getLoc.longitude

        # Add a marker for each urgent care location on the map
        folium.Marker(
            location=[lat, long],
            tooltip=name,
            popup=f"{address}\n{phone}",
            icon=folium.Icon(icon="notes-medical", prefix="fa"),
        ).add_to(m)

    old_html_file_path = "./static/coveragemap.html"
    if os.path.exists(old_html_file_path):
        os.remove(old_html_file_path)

    # Save the map as an HTML file
    m.save(old_html_file_path)
    # <iframe src="./templates/urgencare_map.html" width="800" height="600"></iframe>
