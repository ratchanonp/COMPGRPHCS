import matplotlib.pyplot as plt
import numpy as np

# Define the size of the display
width, height = 100, 100

# Create a 2D array to represent the pixels
pixels = np.zeros((height, width))

# Define the parameters of the parabola y = ax^2 + bx + c
a, b, c = 0.1, 0, 0

# Loop over each pixel
for x in range(width):
    # Calculate the y value of the parabola at this x position
    y = int(a*x**2 + b*x + c)
    # Check if the y value is within the display
    if 0 <= y < height:
        # Set the pixel value to 1
        pixels[height-y-1, x] = 1  # Subtract y from height because the y axis is inverted in the image

# Display the pixels as an image
plt.imshow(pixels, cmap='gray')
plt.show()