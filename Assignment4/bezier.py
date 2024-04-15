import matplotlib.pyplot as plt
import math
import numpy as np

def main():
    jar(show_control=True)
    plt.show()

def jar(show_control=False):
    
    # Body
    body_sections = []

    left = [(9,6), (0 ,13), (15, 23), (5, 26), "left"]
    body_sections.append(left)

    top = [(5,26), (11, 30), (14, 22), (20, 25), "top"]
    body_sections.append(top)

    right = [(20, 25), (16, 21), (28, 13), (18, 6), "right"]
    body_sections.append(right)

    bottom = [(18, 6), (15, 5), (12, 5), (9, 6), "bottom"]
    body_sections.append(bottom)

    # Handle
    handle_section = []

    outter_handle = [(), (25, 30), (30, 20), (), "outter_handle"]
    handle_section.append(outter_handle)

    inner_handle = [(), (24, 28), (28, 20), (), "inner_handle"]
    handle_section.append(inner_handle)

    for section in body_sections:
        control_points, name = section[:-1], section[-1]

        # Find intersection points for the handles
        if name == "right":
            start_outter_handle = find_intersection_at_coor(control_points, x=None, y=21)
            end_outter_handle = find_intersection_at_coor(control_points, x=None, y=11)

            start_inner_handle = find_intersection_at_coor(control_points, x=None, y=19)
            end_inner_handle = find_intersection_at_coor(control_points, x=None, y=13)

            outter_handle[0] = start_outter_handle
            outter_handle[3] = end_outter_handle

            inner_handle[0] = start_inner_handle
            inner_handle[3] = end_inner_handle
        

        plot_curve(control_points, show_control)

    for section in handle_section:
        control_points, name = section[:-1], section[-1]

        plot_curve(control_points, show_control)
    
    # Plot Config
    plt.grid(True)

    plt.gca().set_aspect('equal', adjustable='box')

    plt.xticks(np.arange(-5, 35, 1))
    plt.xticks(rotation=90)
    
    plt.yticks(np.arange(-5, 35, 1))

    plt.tick_params(axis='both', which='major', labelsize=8)

    plt.savefig("Assignment4/jar_bezier.png", dpi=300)
    plt.show()

def find_intersection_at_coor(control_points, x=None, y=None):

    if x is None and y is None:
        return None

    if x is not None:
        u_x = find_u(control_points, x, None)

        if u_x is None:
            raise ValueError("No intersection found")

        x_curve, y_curve = cubic_bezier(control_points, u_x)
        return x_curve, y_curve
    
    if y is not None:
        u_y = find_u(control_points, None, y)

        if u_y is None:
            raise ValueError("No intersection found")

        x_curve, y_curve = cubic_bezier(control_points, u_y)
        return x_curve, y_curve

def find_u(control_points, x=None, y=None):
    INTERVALS = 1000

    u_values = np.linspace(0, 1, INTERVALS)

    for u in u_values:
        x_curve, y_curve = cubic_bezier(control_points, u)

        print(x_curve, y_curve)

        if x is not None:
            if math.isclose(x_curve, x, abs_tol=0.1):
                return u
        
        if y is not None:
            if math.isclose(y_curve, y, abs_tol=0.1):
                return u

    return None

def plot_control_points(control_points):
    x, y = zip(*control_points)
    plt.plot(x, y, 'o')

def plot_curve(control_points, show_control=False):
    INTERVALS = 1000

    u_values = np.linspace(0, 1, INTERVALS)
    x_values = []
    y_values = []

    for u in u_values:
        x, y = cubic_bezier(control_points, u)
        x_values.append(x)
        y_values.append(y)

    plt.plot(x_values, y_values)

    if show_control:
        plot_control_points(control_points)

def cubic_bezier(control_points, u):
    
    M_BEZ = np.array([[-1, 3, -3, 1],
                      [3, -6, 3, 0],
                      [-3, 3, 0, 0],
                      [1, 0, 0, 0]])

    # Split control points to sections of 4
    x_points, y_points = zip(*control_points)
    P_X = np.array(x_points).T
    P_Y = np.array(y_points).T

    # Calculate the point on the curve
    u_vector = np.array([u**3, u**2, u, 1])

    x = np.dot(u_vector, np.dot(M_BEZ, P_X))
    y = np.dot(u_vector, np.dot(M_BEZ, P_Y))

    return x, y

if __name__ == "__main__":
    main()