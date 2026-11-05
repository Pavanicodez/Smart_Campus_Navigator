import time

from algorithms import bfs, ucs, astar


def measure_algorithm(algorithm, start, goal, graph):

    start_time = time.perf_counter()

    if algorithm == "BFS":
        result = bfs(start, goal, graph)

    elif algorithm == "UCS":
        result = ucs(start, goal, graph)

    elif algorithm == "A*":
        result = astar(start, goal, graph)

    else:
        raise ValueError("Invalid algorithm")

    end_time = time.perf_counter()

    if result is None:
        return None

    return {
        "algorithm": algorithm,
        "path": result["path"],
        "cost": result["distance"],
        "nodes_explored": result["nodes_explored"],
        "execution_time": round(
            (end_time - start_time) * 1000, 4
        )
    }


def compare_algorithms(start, goal, graph):

    results = []

    for algorithm in ["BFS", "UCS", "A*"]:

        result = measure_algorithm(
            algorithm, start, goal, graph
        )

        results.append(result)

    return results


def display_metrics(results):

    print("\n========== PERFORMANCE METRICS ==========")

    print(
        f"{'Algorithm':<12}"
        f"{'Cost':<10}"
        f"{'Nodes':<10}"
        f"{'Time (ms)':<12}"
    )

    for result in results:

        print(
            f"{result['algorithm']:<12}"
            f"{result['cost']:<10}"
            f"{result['nodes_explored']:<10}"
            f"{result['execution_time']:<12}"
        )