import numpy as np

def data_generation(N):
    """Generate N random cities and compute the pairwise distance matrix."""

    x = np.round(np.random.rand(N), 2)
    y = np.round(np.random.rand(N), 2)

    city_dict = {i: (x[i], y[i]) for i in range(N)}

    distances = np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            x1, y1 = city_dict[i]
            x2, y2 = city_dict[j]
            distances[i,j] = np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    return x, y, city_dict, distances