import folium
import geocoder
import time

def get_current_location():
    """Function to get the current latitude and longitude"""
    # Use geocoder to get the current location
    location = geocoder.ip('me')
    return location.latlng

def update_map(map_obj):
    """Function to update the map with the current location"""
    while True:
        # Get the current location
        current_location = get_current_location()
        ACTUAL_LOCATION =[12.870001999133143, 80.21851302612968]

        print(current_location)
        
        # Clear previous marker (if any)
        map_obj.children = []
        
        # Add marker for current location
        folium.Marker(location=current_location, popup='code Location').add_to(map_obj)
        folium.Marker(location=ACTUAL_LOCATION, popup='Actual Location').add_to(map_obj)
        
        # Save the map as an HTML file
        map_obj.save("live_location_map.html")
        
        # Wait for some time before updating again
        time.sleep(2)  # Update interval in seconds

def main():
    # Create a map object centered at a default location
    map_obj = folium.Map(location=[0, 0], zoom_start=2)
    
    # Start updating the map with the current location
    update_map(map_obj)

if __name__ == "__main__":
    main()

