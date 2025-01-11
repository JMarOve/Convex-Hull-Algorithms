import numpy as np
from numpy import random
from matplotlib import pyplot as plt
from matplotlib.patches import Patch

def sample_generator(x1: int = 0, y1: int = 500, n: int = 200):
    return [[a, b] for a, b in zip(
        np.random.randint(low=x1, high=y1, size=n),
        np.random.randint(low=x1, high=y1, size=n)
    )]


def vectorbetweenpoints(a, b):
    return [b[0] - a[0], b[1] - a[1]]


def crossproduct(a, b):
    return a[0] * b[1] - a[1] * b[0]


def slope(a, b):
    if a[0] == b[0]:
        return float('inf')
    else:
        return 1.0 * (a[1] - b[1]) / (a[0] - b[0])


def scatter_plot(coords, convex_hull=None, figsize=(12,8)):

    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['Arial']


    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)


    xx = np.linspace(0, 1, 100)
    yy = np.linspace(0, 1, 100)
    X, Y = np.meshgrid(xx, yy)
    Z = 0.7 * np.exp(-(X - 0.5) ** 2 - (Y - 0.5) ** 2)

    plt.imshow(Z, extent=[ax.get_xlim()[0], ax.get_xlim()[1],
                          ax.get_ylim()[0], ax.get_ylim()[1]],
               cmap='Blues', alpha=0.3, aspect='auto')


    xs, ys = zip(*coords)

    if convex_hull is not None:
        non_hull_points = [p for p in coords if p not in convex_hull]
        if non_hull_points:
            non_hull_xs, non_hull_ys = zip(*non_hull_points)
            ax.scatter(non_hull_xs, non_hull_ys,
                       c='#4a90e2',
                       s=150,
                       alpha=0.7,
                       edgecolor='white',
                       linewidth=2,
                       zorder=3,
                       label='Interior Points')

    if convex_hull is not None:
        hull_xs, hull_ys = zip(*convex_hull)
        ax.scatter(hull_xs, hull_ys,
                   c='#1a365d',  # Darker blue for hull points
                   s=180,
                   alpha=0.9,
                   edgecolor='white',
                   linewidth=2,
                   zorder=4,
                   label='Hull Points')

    ax.scatter(coords[0][0], coords[0][1],
               c='#ff6b6b',
               s=200,
               alpha=0.9,
               edgecolor='white',
               linewidth=2,
               zorder=5,
               label='Start Point')
    ax.scatter(coords[0][0], coords[0][1],
               c='#ff6b6b',
               s=300,
               alpha=0.2,
               zorder=4)

    # Plot convex hull lines
    if convex_hull is not None:
        hull_points = convex_hull + [convex_hull[0]]

        # Create hull line with gradient
        for i in range(len(hull_points) - 1):
            x = [hull_points[i][0], hull_points[i + 1][0]]
            y = [hull_points[i][1], hull_points[i + 1][1]]
            ax.plot(x, y,
                    color='#1a365d',  # Matching dark blue
                    linewidth=2.5,
                    linestyle='--',
                    alpha=0.8,
                    zorder=3)

            ax.scatter(x[0], y[0],
                       c='#1a365d',
                       s=100,
                       alpha=0.3,
                       zorder=2)

    ax.grid(True, linestyle='--', alpha=0.2, color='gray')

    # Style the spines
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Title and labels
    ax.set_title('Convex Hull of points',
                 fontsize=16,
                 pad=20,
                 color='#2c3e50',
                 fontweight='bold')

    ax.set_xlabel('X Coordinate',
                  fontsize=12,
                  color='#2c3e50',
                  labelpad=10)

    ax.set_ylabel('Y Coordinate',
                  fontsize=12,
                  color='#2c3e50',
                  labelpad=10)

    ax.tick_params(colors='#2c3e50', length=0)

    legend_elements = [
        Patch(facecolor='none', edgecolor='#1a365d', label='Convex Hull',
              linestyle='--', alpha=0.8),
        plt.Line2D([0], [0], marker='o', color='w',
                   markerfacecolor='#4a90e2', markersize=12,
                   label='Interior Points', alpha=0.7),
        plt.Line2D([0], [0], marker='o', color='w',
                   markerfacecolor='#1a365d', markersize=12,
                   label='Hull Points'),
        plt.Line2D([0], [0], marker='o', color='w',
                   markerfacecolor='#ff6b6b', markersize=12,
                   label='Start Point')
    ]
    ax.legend(handles=legend_elements,
              loc='upper right',
              frameon=True,
              facecolor='white',
              edgecolor='none',
              fontsize=10)

    ax.set_aspect('equal')

    plt.margins(0.2)

    plt.tight_layout()

    return fig, ax
