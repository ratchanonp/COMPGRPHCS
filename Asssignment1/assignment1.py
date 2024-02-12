import matplotlib.pyplot as plt
import numpy as np

def draw_line(x0, y0, x1, y1):
    """Draws a line using Bresenham's line algorithm and matplotlib.

    Args:
        x0 (int): Starting x-coordinate.
        y0 (int): Starting y-coordinate.
        x1 (int): Ending x-coordinate.
        y1 (int): Ending y-coordinate.
    """
    save_x0 = x0
    save_y0 = y0
    save_x1 = x1
    save_y1 = y1

    fig, ax = plt.subplots() # Create a figure containing a single axes.

    # Determine dx and dy
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    # Determine step direction based on slope
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1

    # Initialize error variable
    error = dx - dy

    # Plot starting point
    ax.plot(x0, y0, 'bo')

    while x0 != x1 or y0 != y1:
        # Update coordinates based on Bresenham's algorithm
        e2 = 2 * error
        if e2 > -dy:
            error -= dy
            x0 += sx
        if e2 < dx:
            error += dx
            y0 += sy

        # Plot intermediate points
        ax.plot(x0, y0, 'bo')

    # Ensure last point is plotted
    ax.plot(x1, y1, 'bo')   

    # Set axis limits and labels
    ax.set_xlim(min(save_x0, save_x1) - 1, max(save_x0, save_x1) + 1)
    ax.set_ylim(min(save_y0, save_y1) - 1, max(save_y0, save_y1) + 1)

    ax.set_xticks(np.arange(min(save_x0, save_x1) - 1, max(save_x0, save_x1) + 1, 1))
    ax.set_yticks(np.arange(min(save_y0, save_y1) - 1, max(save_y0, save_y1) + 1, 1))

    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    ax.grid(True)

    # Show the plot
    fig.show()
   
def draw_circle(x_center, y_center, radius):
    x = 0
    y = radius
    p = 1 - radius

    fig, ax = plt.subplots()

    circle_points(x_center, y_center, x, y, ax)

    while x < y:
        x += 1
        if p < 0:
            p = p + 2*x + 1
        else:
            y -= 1
            p = p + 2*x - 2*y + 1

        circle_points(x_center, y_center, x, y, ax)

    
    
    ax.set_xlim([x_center-radius-1, x_center+radius+1])
    ax.set_ylim([y_center-radius-1, y_center+radius+1])
    
    ax.set_xticks(np.arange(x_center-radius-1, x_center+radius+1, 1))
    ax.set_yticks(np.arange(y_center-radius-1, y_center+radius+1, 1))
    ax.grid(True)

    fig.show()

def circle_points(x_center, y_center, x, y, ax):
    ax.plot(x_center + x, y_center + y, marker='o')
    ax.plot(x_center - x, y_center + y, marker='o')
    ax.plot(x_center + x, y_center - y, marker='o')
    ax.plot(x_center - x, y_center - y, marker='o')
    ax.plot(x_center + y, y_center + x, marker='o')
    ax.plot(x_center - y, y_center + x, marker='o')
    ax.plot(x_center + y, y_center - x, marker='o')
    ax.plot(x_center - y, y_center - x, marker='o')

    return ax

def draw_ellipse(x_center, y_center, a, b):
    """Draws an ellipse using the Midpoint Ellipse Algorithm and matplotlib.

    Args:
        x_center (int): X-coordinate of the ellipse's center.
        y_center (int): Y-coordinate of the ellipse's center.
        a (int): Radius in the x-direction.
        b (int): Radius in the y-direction.
    """

    fig, ax = plt.subplots() # Create a figure containing a single axes.

    # Initialize variables
    x = 0
    y = b
    p = b**2 - a**2 * b + a**2 / 4

    # Plot starting points in all four quadrants
    ellipse_points(x_center, y_center, x, y, ax)

    # Region 1
    while a**2 * y > b**2 * x:
        x += 1
        if p < 0:
            p += b**2 * (2 * x + 1)
        else:
            y -= 1
            p += b**2 * (2 * x + 1) + a**2 * (-2 * y + 1)

        ellipse_points(x_center, y_center, x, y, ax)
    
    # Region 2
    while y > 0:
        y -= 1
        if p > 0:
            p += a**2 * (-2 * y + 1)
        else:
            x += 1
            p += b**2 * (2 * x + 1) + a**2 * (-2 * y + 1)

        ellipse_points(x_center, y_center, x, y, ax)

    # Set axis limits and labels
    ax.set_xlim(x_center - a - 1, x_center + a + 1)
    ax.set_ylim(y_center - b - 1, y_center + b + 1)
    ax.set_xticks(np.arange(x_center - a - 1, x_center + a + 1, 1))
    ax.set_yticks(np.arange(y_center - b - 1, y_center + b + 1, 1))
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid(True)

    # Show the plot
    fig.show()

def ellipse_points(x_center, y_center, x, y, ax):
    ax.plot(x_center + x, y_center + y, marker='o')
    ax.plot(x_center - x, y_center + y, marker='o')
    ax.plot(x_center + x, y_center - y, marker='o')
    ax.plot(x_center - x, y_center - y, marker='o')

    return ax

def main():
    shape = input("Enter 'line', 'circle', or 'ellipse': ")
    if shape == 'line':
        x1 = int(input("Enter x1: "))
        y1 = int(input("Enter y1: "))
        x2 = int(input("Enter x2: "))
        y2 = int(input("Enter y2: "))
        draw_line(x1, y1, x2, y2)
    elif shape == 'circle':
        x_center = int(input("Enter x_center: "))
        y_center = int(input("Enter y_center: "))
        radius = int(input("Enter radius: "))
        draw_circle(x_center, y_center, radius)
    elif shape == 'ellipse':
        x_center = int(input("Enter x_center: "))
        y_center = int(input("Enter y_center: "))
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        draw_ellipse(x_center, y_center, a, b)
    else:
        print("Invalid shape")

    plt.show()

if __name__ == "__main__":
    main()