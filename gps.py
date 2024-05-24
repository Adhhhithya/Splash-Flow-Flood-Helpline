from geopy.geocoders import Nominatim
import time

def track_location():
    geolocator = Nominatim(user_agent="geo_tracker")
    while True:
        # Use geolocator to get the location
        location = geolocator.geocode("1600 Amphitheatre Parkway, Mountain View, CA")
        
        # Check if location is found
        if location:
            print("Latitude:", location.latitude)
            print("Longitude:", location.longitude)
        else:
            print("Location not found")
        
        # Wait for some time before checking again
        time.sleep(10)  # Adjust the interval as needed

# Call the function to start tracking the location
track_location()
