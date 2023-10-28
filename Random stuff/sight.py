import pyautogui
import numpy as np

def detect_color(color, region):
    # Get the screen image
    screenshot = pyautogui.screenshot(region=region)
    
    # Convert the image to a numpy array
    image_array = np.array(screenshot)
    
    # Find the coordinates where the color is present
    color_coordinates = np.where(np.all(image_array == color, axis=-1))
    
    return color_coordinates

# Define the RGB values of the color to be detected
color_to_detect = (255, 0, 0)

# Define the region of the screen to search for the color
region_to_search = (0, 0, 1920, 1080)  #top, left , width, height 

# Call the detect_color function
coordinates = detect_color(color_to_detect, region_to_search)

# Check if any coordinates are found
if len(coordinates[0]) > 0:
    # Zip the x and y coordinates together
    coordinate_pairs = list(zip(coordinates[1], coordinates[0]))
    
    # Print the coordinates in a user-friendly format
    for coordinate in coordinate_pairs:
        input(f"Color {color_to_detect} found at coordinates: {coordinate}")
        pyautogui.moveTo(coordinate)
else:
    input(f"No color {color_to_detect} found on the screen.")
