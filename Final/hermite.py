import numpy as np
import matplotlib.pyplot as plt

class HermiteSpline:
    def __init__(self, p_k, p_k1, Dp_K, Dp_k1):
        self.p_k = p_k
        self.p_k1 = p_k1
        self.Dp_K = Dp_K
        self.Dp_k1 = Dp_k1

        self.M_c = np.array([
            [2, -2, 1, 1],
            [-3, 3, -2, -1],
            [0, 0, 1, 0],
            [1, 0, 0, 0]
        ])

    
    def find_point(self, u):
        u_vector = np.array([u ** 3, u ** 2, u, 1])
        x_vector = np.array([self.p_k[0], self.p_k1[0], self.Dp_K, self.Dp_k1])
        y_vector = np.array([self.p_k[1], self.p_k1[1], self.Dp_K, self.Dp_k1])

        x = u_vector @ self.M_c @ x_vector
        y = u_vector @ self.M_c @ y_vector

        return np.array([x, y])
    
def main():
    p_k = np.array([1, 2])
    p_k1 = np.array([4, 3])
    dp_k = 7
    dp_k1 = 5

    plt.plot([p_k[0], p_k1[0]], [p_k[1], p_k1[1]], 'ro')

    spline = HermiteSpline(p_k, p_k1, dp_k, dp_k1)
    for u in [0.3, 0.6]:
        print(f"u = {u}, point = {spline.find_point(u)}")

    plt.show()

if __name__ == "__main__":
    main()

    