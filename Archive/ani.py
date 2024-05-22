import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.interpolate import interp1d
import numpy as np

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# Create the object to animate (a simple square)
object_points = np.array([[-1, -1], [1, -1], [1, 1], [-1, 1], [-1, -1]])

# Create spline for movement trajectory
time_points = np.linspace(0, 1, 100)
x_points = 5 * np.sin(2 * np.pi * time_points)
y_points = 5 * np.cos(2 * np.pi * time_points)

spline_x = interp1d(time_points, x_points, kind='cubic')
spline_y = interp1d(time_points, y_points, kind='cubic')

# Function to perform transformations on the object
def transform_object(object_points, time):
  # Scaling
  scale_factor = 1 + 0.5 * np.sin(4 * np.pi * time)
  scaled_points = object_points * scale_factor

  # Rotation
  angle = 360 * time
  theta = np.radians(angle)
  rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)],
                             [np.sin(theta), np.cos(theta)]])
  rotated_points = np.dot(scaled_points, rotation_matrix.T)

  # Translation
  x_translation = spline_x(time)
  y_translation = spline_y(time)
  translated_points = rotated_points + np.array([x_translation, y_translation])

  # Shearing
  shear_factor = 0.5 * np.sin(2 * np.pi * time)
  shear_matrix = np.array([[1, shear_factor],
                           [0, 1]])
  sheared_points = np.dot(translated_points, shear_matrix.T)

  return sheared_points

# Animation function
def animate(i):
  time = i / 100
  transformed_points = transform_object(object_points, time)
  line.set_data(transformed_points[:, 0], transformed_points[:, 1])
  return line,

# Create the animation
line, = ax.plot([], [], 'r-', linewidth=2)
ani = animation.FuncAnimation(fig, animate, frames=100, interval=20, blit=True)

# Show the animation
plt.show()