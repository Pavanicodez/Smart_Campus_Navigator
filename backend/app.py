from flask import Flask, request, jsonify
from flask_cors import CORS

from graph import CAMPUS_GRAPH
from crowd import get_crowd_adjusted_graph
from metrics import measure_algorithm

app = Flask(__name__)
CORS(app)


# Get all campus locations
@app.route("/api/locations", methods=["GET"])
def get_locations():
    return jsonify(list(CAMPUS_GRAPH.keys()))


# Get campus graph for visualization
@app.route("/api/graph", methods=["GET"])
def get_graph():

    is_lunch_time = (
        request.args.get("lunch", "false").lower() == "true"
    )

    graph = get_crowd_adjusted_graph(is_lunch_time)

    nodes = list(graph.keys())
    edges = []

    # Read connections in both directions
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):

            source = nodes[i]
            destination = nodes[j]

            forward = graph.get(source, {}).get(destination)
            reverse = graph.get(destination, {}).get(source)

            if forward is not None or reverse is not None:

                edges.append({
                    "from": source,
                    "to": destination,
                    "forward_distance": forward,
                    "reverse_distance": reverse
                })

    return jsonify({
        "nodes": nodes,
        "edges": edges
    })


# Find and compare routes
@app.route("/api/route", methods=["POST"])
def find_route():

    data = request.get_json()

    start = data.get("start")
    destination = data.get("destination")
    is_lunch_time = data.get("is_lunch_time", False)

    if not start or not destination:
        return jsonify({
            "error": "Start and destination are required"
        }), 400

    if start not in CAMPUS_GRAPH or destination not in CAMPUS_GRAPH:
        return jsonify({
            "error": "Invalid campus location"
        }), 400

    graph = get_crowd_adjusted_graph(is_lunch_time)

    results = {}

    for algorithm in ["BFS", "UCS", "A*"]:

        raw = measure_algorithm(
            algorithm,
            start,
            destination,
            graph
        )

        if raw is None:
            results[algorithm] = None

        else:
            results[algorithm] = {
                "path": raw["path"],
                "distance": raw["cost"],
                "nodes_explored": raw["nodes_explored"],
                "execution_time": raw["execution_time"]
            }

    return jsonify({
        "start": start,
        "destination": destination,
        "is_lunch_time": is_lunch_time,
        "results": results
    })


if __name__ == "__main__":
    app.run(debug=True)