def knot_vector_generate(knot_type: str, degree_of_polynomial: int, n_control_points: int) -> list[int]:
    if knot_type == "uniform":
        return uniform_knot_vector(degree_of_polynomial, n_control_points)
    elif knot_type == "open":
        return open_knot_vector(degree_of_polynomial, n_control_points)
    else:
        raise ValueError("Invalid knot type")

def uniform_knot_vector(degree_of_polynomial: int, n_control_points: int) -> list[int]:
    knot_vector = []
    for i in range(n_control_points + degree_of_polynomial + 1):
        knot_vector.append(i)
    return knot_vector

def open_knot_vector(degree_of_polynomial: int, n_control_points: int) -> list[int]:
    knot_vector = []
    
    vector_size = n_control_points + degree_of_polynomial + 1

    for j in range(vector_size):
        if j < degree_of_polynomial:
            knot_vector.append(0)
        elif j <= n_control_points:
            knot_vector.append(j - degree_of_polynomial + 1)
        else:
            knot_vector.append(n_control_points - degree_of_polynomial + 2) 

    return knot_vector

def B(k, d, u, knots_vector):
    if d == 1:
        if u >= knots_vector[k] and u < knots_vector[k + 1]:
            return 1
        else:
            return 0
    
    front = (u - knots_vector[k]) / (knots_vector[k + d - 1] - knots_vector[k])
    back = (knots_vector[k + d] - u) / (knots_vector[k + d] - knots_vector[k + 1])

    return front * B(k, d - 1, u, knots_vector) + back * B(k + 1, d - 1, u, knots_vector)



def main():
    degree_of_polynomial = int(input("Enter the degree of polynomial: "))
    n_control_points = int(input("Enter the number of control points: "))
    
    control_points = []

    # for i in range(n_control_points):
    #     x = input(f"Enter x-coordinate of control point {i + 1}: ")
    #     y = input(f"Enter y-coordinate of control point {i + 1}: ")
    #     control_points.append((int(x), int(y)))

    knot_type = input("Enter the knot type (uniform/open/non-uniform): ")


    if knot_type == "non-uniform":
        knots_vector = input("Enter the knot vector: ")
        knots_vector = list(map(int, knots_vector.split()))
    else:
        knots_vector = knot_vector_generate(knot_type, degree_of_polynomial, n_control_points)
    
    print("Knot vector: ", knots_vector)

if __name__ == "__main__":
    main()


