
# Smart Campus Navigator - Test Results

## Project Overview

The Smart Campus Navigator uses graph search algorithms
to find routes between campus locations.

Algorithms implemented:
- Breadth First Search (BFS)
- Uniform Cost Search (UCS)
- A* Search

A crowd penalty is added to routes entering the canteen
during lunch time.

## Test Case 1: Main Gate to Hostel

### Normal Time

| Algorithm | Path Cost | Nodes Explored |
|---|---:|---:|
| BFS | 680 | 10 |
| UCS | 400 | 11 |
| A* | 400 | 4 |

UCS and A* select the minimum-cost route:

Main Gate -> Parking Area -> Canteen -> Hostel

### Lunch Time

| Algorithm | Path Cost | Nodes Explored |
|---|---:|---:|
| BFS | 680 | 10 |
| UCS | 680 | 13 |
| A* | 680 | 5 |

The canteen entry penalty increases its route cost.
UCS and A* select an alternative route:

Main Gate -> Academic Block A -> Library -> Hostel

## Test Case 2: Library to Canteen

| Time Mode | Path Cost |
|---|---:|
| Normal Time | 130 |
| Lunch Time | 430 |

The penalty increases the cost of entering the canteen
by 300 units.

The path remains the same because this test uses
the direct Library-to-Canteen connection.

## Observations

1. BFS finds a path with the minimum number of edges,
   but it does not guarantee minimum weighted distance.
2. UCS finds the minimum-cost path for non-negative
   edge weights.
3. A* uses g(n) + h(n) to guide its search.
4. Lunch-time congestion penalties can change the
   selected minimum-cost route.
5. Nodes explored and execution time are used to
   compare algorithm performance.

## Limitations

- Distances are illustrative sample values.
- Crowd levels use a predefined penalty.
- The current model applies the penalty when entering
  the canteen.
- Live GPS and real-time crowd data are not integrated.

## Conclusion

The prototype demonstrates campus route planning
using BFS, UCS and A*.

The crowd-aware feature demonstrates how route costs
can change during lunch time and how UCS and A*
can select an alternative minimum-cost route.
