from matplotlib import pyplot as plt

def generate_plots(log, city_dict, N, x, y):
    """Plot the fitness over generations and the best route found."""

    _, solution = log[-1]
    route = solution.chromosome

    # Fitness Plot
    fitness_log = [individual.fitness for _, individual in log]

    plt.subplot(1, 2, 1)
    plt.grid()
    ax = plt.gca()
    ax.set_title('Fitness', fontsize=18, weight='bold')
    ax.set_xlabel('Generation')
    plt.plot(fitness_log, color='green')

    # Solution Plot
    x_route = []
    y_route = []
    for city in route:
        xc, yc = city_dict[int(city)]
        x_route.append(xc)
        y_route.append(yc)
    x0, y0 = city_dict[int(route[0])]
    x_route.append(x0)
    y_route.append(y0)

    plt.subplot(1, 2, 2)
    plt.xlim(-0.1, 1.1)
    plt.ylim(-0.1, 1.1)
    plt.grid()
    plt.plot(x, y, 'ro')
    for n in range(N):
        plt.annotate(text=str(n), 
                     xy=(x[n],y[n]), 
                     textcoords='offset points',
                     xytext=(5,5),
                     bbox=dict(boxstyle='round,pad=0.1', fc='yellow', alpha=0.2),
                     )
    plt.plot(x_route, y_route)
    ax = plt.gca()
    ax.set_title('Best solution found', fontsize=18, weight='bold')
    ax.set_aspect('equal', adjustable='box')

    fig = plt.gcf()
    fig.set_size_inches(12, 6)
    fig.canvas.manager.set_window_title('Travelling Salesman Problem')
    plt.show()