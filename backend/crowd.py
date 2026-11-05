from graph import CAMPUS_GRAPH

CROWD_PENALTIES = {
    "Canteen": 300
}


def get_crowd_adjusted_graph(is_lunch_time=False):

    adjusted_graph = {}

    for location, neighbours in CAMPUS_GRAPH.items():

        adjusted_graph[location] = {}

        for neighbour, distance in neighbours.items():

            penalty = 0

            if is_lunch_time and neighbour in CROWD_PENALTIES:
                penalty = CROWD_PENALTIES[neighbour]

            adjusted_graph[location][neighbour] = distance + penalty

    return adjusted_graph