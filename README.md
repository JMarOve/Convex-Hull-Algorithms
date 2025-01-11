# Convex-Hull-Algorithms
 
The convex hull of a set of points is the smallest convex polygon that can enclose all the points. This repo shows the implementation of some of the classical algorithms and some of the newest. I'll focus on 2D. 
My goal is to keep track of the original documentation regarding the algos in the subfolder called **Docs**. Just for the sake of clarity, the convex hull is defined as follows. 

## Definition

Let $P = \{p_1, p_2, \dots, p_n\}$ be a set of $n$ points in the plane. The convex hull, $CH(P)$, is defined as:

$$CH(P) = \bigcap \{H \mid H \text{ is a convex set and } P \subseteq H\}.$$

In layman's terms, the convex hull is the hypersurface that is constructred (in 2d) by stretching a rubber band around the points and letting it snap tight.

## Algorithms

[1] The Graham's scan (1972) [wiki](https://en.wikipedia.org/wiki/Graham_scan). Implemented in [Code](https://github.com/JMarOve/Convex-Hull-Algorithms/blob/main/src/ch_algos/GrahamScan.py)
    Original [paper](https://github.com/JMarOve/Convex-Hull-Algorithms/blob/main/doc/ConvexHull-Graham.pdf)
## To Do:

[-] Jarvis'march (Gift wrapping) (1970) [wiki](https://en.wikipedia.org/wiki/Gift_wrapping_algorithm)

[-] Quickhull (1977) [wiki](https://en.wikipedia.org/wiki/Quickhull)

[-] Divide & Conquer (1977) 

[-] Andy's Algo (Monotone Chaine) (1979) [wiki](https://en.wikibooks.org/wiki/Algorithm_Implementation/Geometry/Convex_hull/Monotone_chain)

[-] Incremental CH (1984) [wiki]()

[-] Kirkpatrick-Seidel (1986) [wiki](https://en.wikipedia.org/wiki/Kirkpatrick%E2%80%93Seidel_algorithm)

[-] Chan's algo (1996) [wiki](https://en.wikipedia.org/wiki/Chan%27s_algorithm)


## Visualization

![Convex Hull Example](https://github.com/JMarOve/Convex-Hull-Algorithms/blob/main/gifs/graham_scan.gif)



