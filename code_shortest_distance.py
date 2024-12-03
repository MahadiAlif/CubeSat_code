import cv2
import numpy as np

def estimate_distance(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to isolate the white page
    _, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    # Find contours in the binary image
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the contour with the maximum area (assuming it's the page)
    page_contour = max(contours, key=cv2.contourArea)

    # Get the bounding box of the page
    x, y, w, h = cv2.boundingRect(page_contour)

    # Calculate the center of the page
    page_center_x = x + w // 2
    page_center_y = y + h // 2

    # Draw a circle at the center of the page (optional)
    cv2.circle(image, (page_center_x, page_center_y), 5, (0, 255, 0), -1)

    # Get the dimensions of the image
    height, width, _ = image.shape

    # Calculate the center of the image
    image_center_x = width // 2
    image_center_y = height // 2

    # Calculate the distance between the centers
    distance_x = image_center_x - page_center_x
    distance_y = image_center_y - page_center_y

    # Calculate the hypotenuse (shortest distance)
    hypotenuse_distance = np.sqrt(distance_x**2 + distance_y**2)

    # Display the image with the circle (optional)
    cv2.imshow('Image with Page Center', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return distance_x, distance_y, hypotenuse_distance

# Replace 'your_image_path.jpg' with the path to your image file
image_path = '13.jpg'
distance_x, distance_y, hypotenuse_distance = estimate_distance(image_path)

print(f"Distance from the center of the page to the center of the image (x, y): ({distance_x}, {distance_y}) pixels")
print(f"Hypotenuse distance: {hypotenuse_distance} pixels")
