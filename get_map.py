from geopy.geocoders import Nominatim
import folium


def create_map(n, a, p):
    loc = Nominatim(user_agent="Geopy Library")


    #replace these with data from scraping
    name = "NextCare Golden" #n
    address = "17121 S Golden Rd, Golden, CO, 80401" #a
    phone = "(720) 506-1332" #p

    getLoc = loc.geocode(address)
    lat, long = getLoc.latitude, getLoc.longitude

    m = folium.Map(location=[lat, long], zoom_start=12)#Stamen Terrain
    folium.Marker(
        location=[lat, long],
        tooltip=name,
        popup=f"{address}\n{phone}",
        icon=folium.Icon(icon="notes-medical", prefix="fa"),
    ).add_to(m)

    m.save("urgentcare_map.html")
    #<iframe src="path/to/your/map.html" width="800" height="600"></iframe>
    m
