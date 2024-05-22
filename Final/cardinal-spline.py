import numpy as np
import matplotlib.pyplot as plt

class CardinalSpline:

    def __init__(self, controls_points, tension=0.5):
        self.controls_points = controls_points
        self.tension = tension
        
        self.n = len(controls_points)
        assert self.n == 4, "Cardinal spline only works with 4 control points"

        # Boundary conditions
        self.P_0 = controls_points[1]
        self.P_1 = controls_points[2]
        self.P_prime_0 = (1 / 2) * (1 - tension) * (controls_points[2] - controls_points[0])
        self.P_prime_1 = (1 / 2) * (1 - tension) * (controls_points[3] - controls_points[1])

        self.s = (1 - tension) / 2

        self.M_c = np.array([
            [-self.s, 2 - self.s, self.s - 2, self.s],
            [2 * self.s, self.s - 3, 3 - 2 * self.s, -self.s],
            [-self.s, 0, self.s, 0],
            [0, 1, 0, 0]
        ])

    def find_point(self, u):
        u_vector = np.array([u ** 3, u ** 2, u, 1])
        P = np.array([self.controls_points[0], self.controls_points[1], self.controls_points[2], self.controls_points[3]])
        return u_vector @ self.M_c @ P
    

def main():
    control_points = [
        np.array([1, 12]),
        np.array([4, 9]),
        np.array([7, 8.5]),
        np.array([9, 11])
    ]   

    plt.scatter([p[0] for p in control_points], [p[1] for p in control_points])

    spline = CardinalSpline(control_points)
    for u in np.linspace(0, 1, 5):
        point = spline.find_point(u)
        print(f"u = {u}, point = {point[0], point[1]}")
        plt.plot(point[0], point[1], 'ro')

    plt.grid()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

if __name__ == "__main__":
    main()

    


