"""
    Write a program to draw an epitrochoid and a hypotrochoid to show what shapes will be drawn
    for the given values:
    (a) 𝑎 = 20, 𝑏 = 15, 𝑘 = 30 with red color and 1-pixel thick
    (b) 𝑎 = 30, 𝑏 = 45, 𝑘 = 20 with green color and 3-pixel thick
    (c) 𝑎 = 50, 𝑏 = 35, 𝑘 = 15 with blue color and 2-pixel thick
    (d) 𝑎 = 15, 𝑏 = 55, 𝑘 = 35 with purple color and 3-pixel thick
"""

import matplotlib.pyplot as plt
from numpy import cos, sin, pi, linspace, lcm


def epitrochoid(ax: plt.Axes, a: int, b: int, k: int, color: str, thickness: int, rev: int = 1) -> None:
    
    t = linspace(0, rev, 1000)

    x = ((a + b) * cos(2 * pi * t)) - (k * cos((2 * pi) * (((a + b) * t) / b)))
    y = ((a + b) * sin(2 * pi * t)) - (k * sin((2 * pi) * (((a + b) * t) / b)))
    
    ax.plot(x, y, color=color, linewidth=thickness)
    ax.set_title(f"Epitrochoid \n a={a}, b={b}, k={k}")
    ax.set_aspect('equal')

def hypotrochoid(ax: plt.Axes, a: int, b: int, k: int, color: str, thickness: int, rev: int = 1) -> None:

    t = linspace(0, rev, 1000)

    x = ((a - b) * cos(2 * pi * t)) + (k * cos((2 * pi) * (((a - b) * t) / b)))
    y = ((a - b) * sin(2 * pi * t)) - (k * sin((2 * pi) * (((a - b) * t) / b)))

    ax.plot(x, y, color=color, linewidth=thickness)
    ax.set_title(f"Hypotrochoid \n a={a}, b={b}, k={k}")
    ax.set_aspect('equal')

def main():

    problem = [
        {
            "name": "a",
            "a": 20,
            "b": 15,
            "k": 30,
            "color": "red",
            "thickness": 1,
            "rev": 3
        },
        {
            "name": "b",
            "a": 30,
            "b": 45,
            "k": 20,
            "color": "green",
            "thickness": 3,
            "rev": 3
        },
        {
            "name": "c",
            "a": 50,
            "b": 35,
            "k": 15,
            "color": "blue",
            "thickness": 2,
            "rev": 7
        },
        {
            "name": "d",
            "a": 15,
            "b": 55,
            "k": 35,
            "color": "purple",
            "thickness": 3,
            "rev": 11
        }
    ]

    for p in problem:
        a, b, k = p["a"], p["b"], p["k"]
        color, thickness = p["color"], p["thickness"]
        rev = p["rev"]

        fig, (epitrochoid_ax, hypotrochoid_ax) = plt.subplots(1, 2)
        epitrochoid(epitrochoid_ax, a, b, k, color, thickness, rev)
        hypotrochoid(hypotrochoid_ax, a, b, k, color, thickness, rev)

        plt.savefig(f"Assignment3/Assignment3_{p['name']}.png")

        plt.show()

if __name__ == "__main__":
    main()