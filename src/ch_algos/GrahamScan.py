from src.utils import *
import matplotlib.animation as animation
from IPython.display import HTML
def grahamscan(points):
    # First step is sorting the points. We look for the point with smallest x value.
    # If there are two points with min x-value we take the one with the smallest y-value.

    points.sort(key=lambda x: [x[0], x[1]])
    origin = points.pop(0)

    # We order the points by its slope wrt the origin.
    # If two points have the same slope, we consider the one which is closer to the height level.
    # Last case is that it must be furthest away.

    points.sort(key=lambda x: (slope(x, origin), -x[1], x[0]))

    # Now adding 3 points sequentially forming a convex angle.
    # We compute if three points are right turn or left turn by means of cross product.
    # Just remember that axb=¦¦a¦¦x¦¦b¦¦xSin(z) where z is the angle between a and b in Euclidean woke geometry
    # In affine coordinates, if P1P2 and P1P3 are the vectors, we have that
    # P1P2 X P1P3 = (X2-X1)*(Y3-Y1) -(X3-X1)*(Y2-Y1)
    # If result is 0, then points collinear, if result is positive then left turn, otherwise right turn.
    # If it's left turn, we delete the medium point.

    convexhull = [origin]

    for point in points:
        convexhull.append(point)
        while len(convexhull) > 2 and crossproduct(
                vectorbetweenpoints(convexhull[-2], convexhull[-3]),
                vectorbetweenpoints(convexhull[-1], convexhull[-2])
        ) < 0:
            convexhull.pop(-2)

    return convexhull


def animate_grahamscan(points, save_path='../gifs/graham_scan.gif', interval=100):
    points_copy = points.copy()
    points_copy.sort(key=lambda x: [x[0], x[1]])
    origin = points_copy.pop(0)
    points_copy.sort(key=lambda x: (slope(x, origin), -x[1], x[0]))


    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['Arial']

    fig = plt.figure(figsize=(18, 15))
    ax = fig.add_subplot(111)


    xx = np.linspace(0, 1, 100)
    yy = np.linspace(0, 1, 100)
    X, Y = np.meshgrid(xx, yy)
    Z = 0.7 * np.exp(-(X - 0.5) ** 2 - (Y - 0.5) ** 2)

    def init():
        ax.clear()
        plt.imshow(Z, extent=[ax.get_xlim()[0]-10, ax.get_xlim()[1]+10,
                              ax.get_ylim()[0]-10, ax.get_ylim()[1]+10],
                   cmap='Blues', alpha=0.3, aspect='auto')
        return []

    def animate(frame):
        ax.clear()

        plt.imshow(Z, extent=[ax.get_xlim()[0]-10, ax.get_xlim()[1]+10,
                              ax.get_ylim()[0]-10, ax.get_ylim()[1]+10],
                   cmap='Blues', alpha=0.3, aspect='auto')

        ax.grid(True, linestyle='--', alpha=0.2, color='gray')

        for spine in ax.spines.values():
            spine.set_visible(False)

        xs, ys = zip(*points)
        ax.scatter(xs, ys, c='#4a90e2', s=150, alpha=0.7,
                   edgecolor='white', linewidth=2, zorder=3,
                   label='Points')

        ax.scatter(origin[0], origin[1], c='#ff6b6b', s=200,
                   alpha=0.9, edgecolor='white', linewidth=2,
                   zorder=5, label='Start Point')
        ax.scatter(origin[0], origin[1], c='#ff6b6b', s=300,
                   alpha=0.2, zorder=4)

        current_hull = [origin]
        if frame > 0:
            for i in range(min(frame, len(points_copy))):
                current_hull.append(points_copy[i])
                while len(current_hull) > 2 and crossproduct(
                        vectorbetweenpoints(current_hull[-2], current_hull[-3]),
                        vectorbetweenpoints(current_hull[-1], current_hull[-2])
                ) < 0:
                    current_hull.pop(-2)

        if len(current_hull) > 1:
            hull_xs, hull_ys = zip(*current_hull)
            # Plot hull points
            ax.scatter(hull_xs, hull_ys, c='#1a365d', s=180,
                       alpha=0.9, edgecolor='white', linewidth=2,
                       zorder=4, label='Hull Points')

            for i in range(len(current_hull) - 1):
                ax.plot([current_hull[i][0], current_hull[i + 1][0]],
                        [current_hull[i][1], current_hull[i + 1][1]],
                        color='#1a365d', linewidth=2.5,
                        linestyle='--', alpha=0.8, zorder=3)

            if frame == len(points_copy):
                ax.plot([current_hull[-1][0], current_hull[0][0]],
                        [current_hull[-1][1], current_hull[0][1]],
                        color='#1a365d', linewidth=2.5,
                        linestyle='--', alpha=0.8, zorder=3)

        ax.set_title('Graham Scan Algorithm\nStep ' + str(frame),
                     fontsize=16, pad=20, color='#2c3e50',
                     fontweight='bold')
        ax.set_xlabel('X Coordinate', fontsize=12, color='#2c3e50',
                      labelpad=10)
        ax.set_ylabel('Y Coordinate', fontsize=12, color='#2c3e50',
                      labelpad=10)

        ax.tick_params(colors='#2c3e50', length=0)

        legend_elements = [
            plt.Line2D([0], [0], marker='o', color='w',
                       markerfacecolor='#4a90e2', markersize=12,
                       label='Points', alpha=0.7),
            plt.Line2D([0], [0], marker='o', color='w',
                       markerfacecolor='#1a365d', markersize=12,
                       label='Hull Points'),
            plt.Line2D([0], [0], marker='o', color='w',
                       markerfacecolor='#ff6b6b', markersize=12,
                       label='Start Point'),
            Patch(facecolor='none', edgecolor='#1a365d',
                  label='Hull Edge', linestyle='--', alpha=0.8)
        ]
        ax.legend(handles=legend_elements, loc='upper right',
                  frameon=True, facecolor='white', edgecolor='none',
                  fontsize=10)

        ax.set_aspect('equal')
        plt.margins(0.2)

        return []

    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=len(points_copy) + 1,
                                   interval=interval, blit=True)

    anim.save(save_path, writer='pillow')

    plt.close()

    return HTML(f'<img src="{save_path}">')
