from geopy.geocoders import Nominatim
import folium


def create_map(urgent_care_list, userZip):
    loc = Nominatim(user_agent="Geopy Library")
    m = folium.Map(location=[loc.geocode(userZip).latitude, loc.geocode(userZip).longitude], zoom_start=12)

    if not urgent_care_list:
        urgent_care_list = [1]
        
    for urgent_care in urgent_care_list:
        #replace these with data from scraping
        name = urgent_care['fullName']
        address = urgent_care['address']['line1'] + " ," + urgent_care['address']['city'] + " ," + urgent_care['address']['state'] + " ," + urgent_care['address']['zip']
        phone = urgent_care["phone"]

        getLoc = loc.geocode(address)
        lat, long = getLoc.latitude, getLoc.longitude

    
        folium.Marker(
            location=[lat, long],
            tooltip=name,
            popup=f"{address}\n{phone}",
            icon=folium.Icon(icon="notes-medical", prefix="fa"),
        ).add_to(m)

        m.save("./static/coveragemap.html")
        #<iframe src="./templates/urgencare_map.html" width="800" height="600"></iframe>
