def lorenz(r, sigma=10, b=8 / 3):
    f1 = lambda x, y, z: -sigma * x + sigma * y
    f2 = lambda x, y, z: -x * z + r * x - y
    f3 = lambda x, y, z: x * y - b * z

    return f1, f2, f3
