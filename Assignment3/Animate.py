import matplotlib.pyplot as plt
import matplotlib.animation as animation
from numpy import cos, sin, pi, linspace


def epitrochoid(a: int, b: int, k: int, t: float) -> tuple[float, float]:
    x = ((a + b) * cos(2 * pi * t)) - (k * cos((2 * pi) * (((a + b) * t) / b)))
    y = ((a + b) * sin(2 * pi * t)) - (k * sin((2 * pi) * (((a + b) * t) / b)))
    return x, y

def hypotrochoid(a: int, b: int, k: int, t: float) -> tuple[float, float]:
    x = ((a - b) * cos(2 * pi * t)) + (k * cos((2 * pi) * (((a - b) * t) / b)))
    y = ((a - b) * sin(2 * pi * t)) - (k * sin((2 * pi) * (((a - b) * t) / b)))
    return x, y

def update(num, a, b, k, line, func):
    t = linspace(0, num/100, 1000)
    x, y = func(a, b, k, t)
    line.set_data(x, y)
    return line,

def animate(*args, **kwargs):

    a, b, k, color, thickness, rev, func = kwargs["a"], kwargs["b"], kwargs["k"], kwargs["color"], kwargs["thickness"], kwargs["rev"], kwargs["func"]

    fig, ax = plt.subplots()
    line, = ax.plot([], [], color=color, linewidth=thickness)
    ax.set_xlim(-100, 100)
    ax.set_ylim(-100, 100)
    ax.set_title(f"Epitrochoid \n a={a}, b={b}, k={k}")

    ani = animation.FuncAnimation(fig, update, frames=range(0, rev*100), fargs=[a, b, k, line, func], interval=17, blit=True)
    ani.save(f"Assignment3/result/{kwargs['name']}.mp4", writer="ffmpeg", fps=60)
    plt.show()

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
        name = p["name"]
        a, b, k = p["a"], p["b"], p["k"]
        color, thickness = p["color"], p["thickness"]
        rev = p["rev"]

        animate(name=f"{name}_epitrochoid", a=a, b=b, k=k, color=color, thickness=thickness, rev=rev, func=epitrochoid)
        animate(name=f"{name}_hypotrochoid", a=a, b=b, k=k, color=color, thickness=thickness, rev=rev, func=hypotrochoid)

if __name__ == "__main__":
    main()