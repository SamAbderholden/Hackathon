from geopy.geocoders import Nominatim
import folium


def create_map(urgent_care_list):
    loc = Nominatim(user_agent="Geopy Library")
    m = folium.Map(location=[lat, long], zoom_start=12)

    if not urgent_care_list:
        urgent_care_list = [1]
        
    for urgent_care in urgent_care_list:
        #replace these with data from scraping
        name = "NextCare Golden" #urgent_care["name"]
        address = "17121 S Golden Rd, Golden, CO, 80401" #urgent_care["address"]
        phone = "(720) 506-1332" #urgent_care["phone"]

        getLoc = loc.geocode(address)
        lat, long = getLoc.latitude, getLoc.longitude

    
        folium.Marker(
            location=[lat, long],
            tooltip=name,
            popup=f"{address}\n{phone}",
            icon=folium.Icon(icon="notes-medical", prefix="fa"),
        ).add_to(m)

        m.save("urgentcare_map.html")
        #<iframe src="path/to/your/map.html" width="800" height="600"></iframe>
