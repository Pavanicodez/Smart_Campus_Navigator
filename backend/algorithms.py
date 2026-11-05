import heapq
from collections import deque
from itertools import count

from graph import CAMPUS_GRAPH


def _validate_locations(start, goal, graph):

    if start not in graph or goal not in graph:
        raise ValueError("Unknown campus location")


def bfs(start, goal, graph=None):

    if graph is None:
        graph = CAMPUS_GRAPH

    _validate_locations(start, goal, graph)

    queue = deque([(start, [start])])

    visited = {start}
    explored = 0

    while queue:

        current, path = queue.popleft()

        explored += 1

        if current == goal:

            distance = sum(
                graph[a][b]
                for a, b in zip(path, path[1:])
            )

            return {
                "path": path,
                "distance": distance,
                "nodes_explored": explored
            }

        for neighbour in graph[current]:

            if neighbour not in visited:

                visited.add(neighbour)

                queue.append((neighbour, path + [neighbour]))

    return None


def ucs(start, goal, graph=None):

    if graph is None:
        graph = CAMPUS_GRAPH

    _validate_locations(start, goal, graph)

    counter = count()

    priority_queue = [
        (0, next(counter), start, [start])
    ]

    best_cost = {start: 0}

    explored = 0

    while priority_queue:

        cost, _, current, path = heapq.heappop(priority_queue)

        if cost != best_cost.get(current):
            continue

        explored += 1

        if current == goal:

            return {
                "path": path,
                "distance": cost,
                "nodes_explored": explored
            }

        for neighbour, edge_cost in graph[current].items():

            new_cost = cost + edge_cost

            if new_cost < best_cost.get(neighbour, float("inf")):

                best_cost[neighbour] = new_cost

                heapq.heappush(
                    priority_queue,
                    (
                        new_cost,
                        next(counter),
                        neighbour,
                        path + [neighbour]
                    )
                )

    return None


def build_heuristic(graph, goal):

    reverse_graph = {
        node: {} for node in graph
    }

    for node, neighbours in graph.items():

        for neighbour, edge_cost in neighbours.items():

            reverse_graph[neighbour][node] = edge_cost

    counter = count()

    priority_queue = [
        (0, next(counter), goal)
    ]

    distances = {goal: 0}

    while priority_queue:

        cost, _, current = heapq.heappop(priority_queue)

        if cost != distances.get(current):
            continue

        for neighbour, edge_cost in reverse_graph[current].items():

            new_cost = cost + edge_cost

            if new_cost < distances.get(neighbour, float("inf")):

                distances[neighbour] = new_cost

                heapq.heappush(
                    priority_queue,
                    (new_cost, next(counter), neighbour)
                )

    return distances


def astar(start, goal, graph=None):

    if graph is None:
        graph = CAMPUS_GRAPH

    _validate_locations(start, goal, graph)

    heuristic = build_heuristic(graph, goal)

    counter = count()

    priority_queue = [
        (heuristic[start], next(counter), 0, start, [start])
    ]

    best_cost = {start: 0}

    explored = 0

    while priority_queue:

        _, _, cost, current, path = heapq.heappop(priority_queue)

        if cost != best_cost.get(current):
            continue

        explored += 1

        if current == goal:

            return {
                "path": path,
                "distance": cost,
                "nodes_explored": explored
            }

        for neighbour, edge_cost in graph[current].items():

            new_cost = cost + edge_cost

            if new_cost < best_cost.get(neighbour, float("inf")):

                best_cost[neighbour] = new_cost

                estimated_total = new_cost + heuristic[neighbour]

                heapq.heappush(
                    priority_queue,
                    (
                        estimated_total,
                        next(counter),
                        new_cost,
                        neighbour,
                        path + [neighbour]
                    )
                )

    return None