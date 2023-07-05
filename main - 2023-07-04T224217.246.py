import requests

def find_closest_gas_station(api_key, latitude, longitude):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "key": api_key,
        "location": f"{latitude},{longitude}",
        "radius": 5000,  # Search within a 5000-meter radius (adjust as needed)
        "keyword": "gas station"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data["status"] == "OK":
        results = data["results"]
        if results:
            # Extract details of the closest gas station
            closest_station = results[0]
            name = closest_station["name"]
            vicinity = closest_station["vicinity"]
            location = closest_station["geometry"]["location"]
            lat = location["lat"]
            lng = location["lng"]

            print("Closest Gas Station:")
            print(f"Name: {name}")
            print(f"Address: {vicinity}")
            print(f"Latitude: {lat}")
            print(f"Longitude: {lng}")
        else:
            print("No gas stations found nearby.")
    else:
        print("Error occurred while retrieving data.")

# Set your API key and coordinates (latitude and longitude)
API_KEY = "YOUR_API_KEY"
latitude = 37.7749  # Example latitude (San Francisco)
longitude = -122.4194  # Example longitude (San Francisco)

find_closest_gas_station(API_KEY, latitude, longitude)

