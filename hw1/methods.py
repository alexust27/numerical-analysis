import numpy as np

class Method:
    def __init__(self, f, h=0.01):
        self.f1, self.f2, self.f3 = f
        self.h = h

    def apply(self, vec):
        [x, y, z] = vec
        return np.array([self.f1(x, y, z), self.f2(x, y, z), self.f3(x, y, z)])

    def get_points(self, vec0, n=1000):
        [x, y, z] = [[t] for t in vec0]
        vec = vec0
        for i in range(0, n):
            vec = self.next_iteration(vec)
            x.append(vec[0])
            y.append(vec[1])
            z.append(vec[2])

        return x, y, z

    def next_iteration(self, vec):
        pass

    def get_method_name(self):
        pass

class ExplicitEuler(Method):
    def next_iteration(self, vec):
        return self.h * self.apply(vec) + vec

    def get_method_name(self):
        return 'Явный метод Эйлера'

class ImplicitEuler(Method):
    def next_iteration(self, vec):
        vec0 = self.h * self.apply(vec) + vec
        return vec + self.h / 2 * (self.apply(vec0) + self.apply(vec))

    def get_method_name(self):
        return 'Неявный метод Эйлера'

class RungeKutta(Method):
    def next_iteration(self, vec):
        k1 = self.apply(vec)
        k2 = self.apply(vec + (k1 * self.h / 2))
        k3 = self.apply(vec + (k2 * self.h / 2))
        k4 = self.apply(vec + (k3 * self.h))
        return vec + ((k1 + k2 * 2 + k3 * 3 + k4) * self.h / 6)

    def get_method_name(self):
        return 'Метод Рунге-Кутта'

class Adams(Method):
    def __init__(self, vec0, f, h=0.01):
        super().__init__(f, h=h)

        runge_kutta = RungeKutta(f, h=h)
        vec1 = runge_kutta.next_iteration(vec0)
        vec2 = runge_kutta.next_iteration(vec1)
        vec3 = runge_kutta.next_iteration(vec2)
        self.mas_arr = [vec0, vec1, vec2, vec3]

    def next_iteration(self, vec):
        f0 = self.apply(self.mas_arr[0])
        f1 = self.apply(self.mas_arr[1])
        f2 = self.apply(self.mas_arr[2])
        f3 = self.apply(vec)

        y0 = vec + self.h / 24 * (55 * f3 - 59 * f2 + 37 * f1 - 9 * f0)
        f40 = self.apply(y0)

        self.mas_arr[0] = self.mas_arr[1]
        self.mas_arr[1] = self.mas_arr[2]
        self.mas_arr[2] = vec
        new_f = vec + self.h / 24 * (9 * f40 + 19 * f3 - 5 * f2 + f1)
        self.mas_arr[3] = new_f
        return new_f

    def get_method_name(self):
        return 'Метод Адамса'
