import matplotlib.pyplot as plt
import math
import numpy as np

def main():

    print("What do you want to draw?")
    print("[1] Jar (preset)")
    print("[2] Custom")
    print("[3] Dev Mode")
    choice = int(input("Enter choice: "))

    if choice == 1:
        jar(show_control=True)
    elif choice == 2:
        custom()
    elif choice == 3:
        dev_mode()
   
    plt.show()

def custom():
    control_points = []

    degree_of_polynomail = int(input("Degree of polynomial (b-spline): "))
    number_of_spline = int(input("Number of spline: "))

    for _ in range(number_of_spline):
        spline_control_points = []
        while True:
            corr = tuple(map(int, input("Enter control point (x, y): ").split()))

            if corr == (-1, -1):
                break
            
            spline_control_points.append(corr)
        
        b_spline_point = b_spline(degree_of_polynomail, control_points)
        bezier_point = bezier(control_points)

        plt.plot(*zip(*b_spline_point), label="B-Spline")
        plt.plot(*zip(*bezier_point), label="Bezier")

def dev_mode():

    sections = []

    sections.append([(9,6), (0 ,13), (15, 23), (5, 26)])
    
    for section in sections:
        control_points = section

        bezier_point = bezier(control_points)

        plt.plot(*zip(*bezier_point), "r-")
        plt.plot(*zip(*control_points), "bo")

    # Plot Config
    plt.grid(True)

    plt.gca().set_aspect('equal', adjustable='box')

    plt.xticks(np.arange(-5, 35, 1))
    plt.xticks(rotation=90)
    
    plt.yticks(np.arange(-5, 35, 1))

    plt.tick_params(axis='both', which='major', labelsize=8)

    plt.savefig("Assignment4/jar_cubic_bezier.png", dpi=300)

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

    shaped_points = []

    for section in body_sections:
        control_points, name = section[:-1], section[-1]
        
        section_curve_points = cubic_bezier(control_points)
        shaped_points.append(section_curve_points)

        # Find intersection points for the handles
        if name == "right":
            start_outter_handle = find_intersection_at_coor(section_curve_points, x=None, y=21)
            end_outter_handle = find_intersection_at_coor(section_curve_points, x=None, y=11)

            start_inner_handle = find_intersection_at_coor(section_curve_points, x=None, y=19)
            end_inner_handle = find_intersection_at_coor(section_curve_points, x=None, y=13)

            outter_handle[0] = start_outter_handle
            outter_handle[3] = end_outter_handle

            inner_handle[0] = start_inner_handle
            inner_handle[3] = end_inner_handle


    for section in handle_section:
        control_points, name = section[:-1], section[-1]

        section_curve_points = cubic_bezier(control_points)
        shaped_points.append(section_curve_points)

    for section in shaped_points:
        plt.plot(*zip(*section), 'r-')
    
    
    # Plot Config
    plt.grid(True)

    plt.gca().set_aspect('equal', adjustable='box')

    plt.xticks(np.arange(-5, 35, 1))
    plt.xticks(rotation=90)
    
    plt.yticks(np.arange(-5, 35, 1))

    plt.tick_params(axis='both', which='major', labelsize=8)

    plt.savefig("Assignment4/jar_cubic_bezier.png", dpi=300)

    plt.legend()

    plt.show()

def find_intersection_at_coor(section_curve_points: list[tuple[int, int]], x=None, y=None):
    """
    Find the intersection point at the given x or y coordinate
    NOTE: this function use to find coordinate to find a perfect point to attach jar handle to jar body
    """
    if x:
        for (x_point, y_point) in section_curve_points:
            if math.isclose(x_point, x, abs_tol=0.1):
                return (x_point, y_point)
        
    elif y:
        for (x_point, y_point) in section_curve_points:
            if math.isclose(y_point, y, abs_tol=0.1):
                return (x_point, y_point)
    
    return None

def cubic_bezier(control_points: list[tuple[int, int]]) -> list[tuple[int, int]]:
    
    M_BEZ = np.array([[-1, 3, -3, 1],
                      [3, -6, 3, 0],
                      [-3, 3, 0, 0],
                      [1, 0, 0, 0]])

    # Split control points to sections of 4
    x_points, y_points = zip(*control_points)
    P_X = np.array(x_points).T
    P_Y = np.array(y_points).T

    INTERVALS = 1000

    points = []

    # Calculate the point on the curve
    for u in np.linspace(0, 1, INTERVALS):
        u_vector = np.array([u**3, u**2, u, 1])
        x = np.dot(u_vector, np.dot(M_BEZ, P_X))
        y = np.dot(u_vector, np.dot(M_BEZ, P_Y))

        points.append((x, y))
    return points

def bezier(control_points: list[tuple[int, int]]) -> list[tuple[int, int]]:
    degree_of_polynomial = len(control_points) - 1

    if degree_of_polynomial == 3:
        return cubic_bezier(control_points)

    coefficient = compute_coefficient(degree_of_polynomial)

    INTERVALS = 1000
    points = []

    for u in np.linspace(0, 1, INTERVALS):
        x = 0
        y = 0

        for i in range(degree_of_polynomial + 1):
            x += coefficient[i] * control_points[i][0] * (1 - u)**(degree_of_polynomial - i) * u**i
            y += coefficient[i] * control_points[i][1] * (1 - u)**(degree_of_polynomial - i) * u**i

        points.append((x, y))

    return points

def compute_coefficient(degree_of_polynomial: int) -> list[int]:
    coefficients = []

    for i in range(degree_of_polynomial + 1):
        coefficient = math.comb(degree_of_polynomial, i)
        coefficients.append(coefficient)

    return coefficients

def b_spline(degree_of_polynomial: int, control_points: list[tuple[int,int]]) -> list[tuple[int, int]]:
    return [()]

if __name__ == "__main__":
    main()