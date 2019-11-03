from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

from methods import Adams, ExplicitEuler, ImplicitEuler, RungeKutta
from data import lorenz

def draw_graphics(r, vec0):
    fig = plt.figure()
    axes = Axes3D(fig)
    axes.set_xlabel('x')
    axes.set_ylabel('y')
    axes.set_zlabel('z')

    x, y, z = ExplicitEuler(lorenz(r)).get_points(vec0)
    axes.plot(x, y, z, label='явный метод Эйлера')
    x, y, z = ImplicitEuler(lorenz(r)).get_points(vec0)
    axes.plot(x, y, z, label='неявный метод Эйлера')
    x, y, z = RungeKutta(lorenz(r)).get_points(vec0)
    axes.plot(x, y, z, label='метод Рунге-Кутта')
    x, y, z = Adams(vec0, lorenz(r)).get_points(vec0)
    axes.plot(x, y, z, label='метод Адамса')

    axes.legend()
    plt.show()

def draw_graphic(vec0, method):
    fig = plt.figure()
    axes = Axes3D(fig)
    axes.set_xlabel('x')
    axes.set_ylabel('y')
    axes.set_zlabel('z')
    axes.set_title(method.get_method_name())

    x, y, z = method.get_points(vec0)
    axes.plot(x, y, z)

    plt.show()
