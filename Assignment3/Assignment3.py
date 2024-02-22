"""
    Write a program to draw an epitrochoid and a hypotrochoid to show what shapes will be drawn
    for the given values:
    (a) 𝑎 = 20, 𝑏 = 15, 𝑘 = 30 with red color and 1-pixel thick
    (b) 𝑎 = 30, 𝑏 = 45, 𝑘 = 20 with green color and 3-pixel thick
    (c) 𝑎 = 50, 𝑏 = 35, 𝑘 = 15 with blue color and 2-pixel thick
    (d) 𝑎 = 15, 𝑏 = 55, 𝑘 = 35 with purple color and 3-pixel thick
"""

import matplotlib.pyplot as plt
import numpy as np

def epitrochoid(ax: plt.Axes, a: int, b: int, k: int, color: str, thickness: int) -> None:
    t = np.linspace(0, 2 * np.pi, 1000)
    x = (a + b) * np.cos(t) - k * np.cos((a + b) / b * t)
    y = (a + b) * np.sin(t) - k * np.sin((a + b) / b * t)
    ax.plot(x, y, color=color, linewidth=thickness)
    ax.set_title(f"Epitrochoid \n a={a}, b={b}, k={k}")

def hypotrochoid(ax: plt.Axes, a: int, b: int, k: int, color: str, thickness: int) -> None:
    t = np.linspace(0, 2 * np.pi, 1000)
    x = (a - b) * np.cos(t) + k * np.cos((a - b) / b * t)
    y = (a - b) * np.sin(t) - k * np.sin((a - b) / b * t)
    ax.plot(x, y, color=color, linewidth=thickness)
    ax.set_title(f"Hypotrochoid \n a={a}, b={b}, k={k}")

def main():
    # (a) 𝑎 = 20, 𝑏 = 15, 𝑘 = 30 with red color and 1-pixel thick
    fig, (epitrochoid_ax, hypotrochoid_ax) = plt.subplots(1, 2)
    epitrochoid(epitrochoid_ax, 20, 15, 30, 'red', 1)
    hypotrochoid(hypotrochoid_ax, 20, 15, 30, 'red', 1)
    fig.savefig(f"Assignment3/Assignment3_a.png")

    # (b) 𝑎 = 30, 𝑏 = 45, 𝑘 = 20 with green color and 3-pixel thick
    fig, (epitrochoid_ax, hypotrochoid_ax) = plt.subplots(1, 2)
    epitrochoid(epitrochoid_ax, 30, 45, 20, 'green', 3)
    hypotrochoid(hypotrochoid_ax, 30, 45, 20, 'green', 3)
    fig.savefig(f"Assignment3/Assignment3_b.png")

    # (c) 𝑎 = 50, 𝑏 = 35, 𝑘 = 15 with blue color and 2-pixel thick
    fig, (epitrochoid_ax, hypotrochoid_ax) = plt.subplots(1, 2)
    epitrochoid(epitrochoid_ax, 50, 35, 15, 'blue', 2)
    hypotrochoid(hypotrochoid_ax, 50, 35, 15, 'blue', 2)
    fig.savefig(f"Assignment3/Assignment3_c.png")

    # (d) 𝑎 = 15, 𝑏 = 55, 𝑘 = 35 with purple color and 3-pixel thick
    fig, (epitrochoid_ax, hypotrochoid_ax) = plt.subplots(1, 2)
    epitrochoid(epitrochoid_ax, 15, 55, 35, 'purple', 3)
    hypotrochoid(hypotrochoid_ax, 15, 55, 35, 'purple', 3)
    fig.savefig(f"Assignment3/Assignment3_d.png")

    plt.show()

if __name__ == "__main__":
    main()