import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to create a basic animation
def animate(i):
    ax.clear()
    
    # Rotation matrix
    theta = np.radians(i * 4)
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    
    # Scaling matrix
    scaling_matrix = np.array([[1 + i * 0.01, 0], [0, 1 + i * 0.01]])
    
    # Translation vector
    translation_vector = np.array([i * 0.1, i * 0.1])
    
    # Shearing matrix
    shear_matrix = np.array([[1, i * 0.01], [0, 1]])
    
    # Apply transformation to a square
    square = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]])
    transformed_square = square.dot(rotation_matrix).dot(scaling_matrix) + translation_vector
    transformed_square = transformed_square.dot(shear_matrix)
    
    ax.plot(transformed_square[:,0], transformed_square[:,1], color='blue')

# Create a figure and axis
fig, ax = plt.subplots()

# Set axis limits
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

# Create animation
ani = FuncAnimation(fig, animate, frames=180, interval=50)

# Show animation
plt.show()
