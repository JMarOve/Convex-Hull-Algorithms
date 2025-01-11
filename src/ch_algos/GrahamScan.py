from src.utils import *
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

