# Smart Campus Navigator
### Time-Aware Route Planning Using BFS, UCS and A* Search

## 1. Project Overview

Smart Campus Navigator is a web-based campus navigation prototype that helps users find routes between campus locations.

The system compares three search algorithms:

- Breadth-First Search (BFS)
- Uniform Cost Search (UCS)
- A* Search

It also provides Normal Time and Lunch Time modes. In Lunch Time mode, simulated crowd penalties are applied to selected paths to demonstrate how changing conditions can affect route costs.

The application displays route details, algorithm performance comparisons, and a visual representation of the campus graph.

## 2. Objectives

- Represent campus locations and connections using a weighted graph.
- Implement BFS, UCS and A* search algorithms.
- Find and compare routes between selected locations.
- Simulate lunch-time crowd conditions.
- Compare algorithms using route cost, nodes explored and execution time.
- Visualize the campus graph and highlight selected routes.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend logic and search algorithms |
| Flask | Backend API development |
| Flask-CORS | Communication between frontend and backend |
| HTML | Webpage structure |
| CSS | User interface styling |
| JavaScript | Frontend interaction and API communication |
| SVG | Campus graph visualization |

## 4. Project Structure

```text
Smart-Campus-Navigator/
│
├── backend/
│   ├── graph.py
│   ├── algorithms.py
│   ├── crowd.py
│   ├── metrics.py
│   └── app.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   ├── graph.js
│   └── app.py
│
├── tests/
│   └── test_algorithms.py
│
├── docs/
│   └── screenshots/
│
├── campus_data.json
└── README.md
```

## 5. Methodology

### 5.1 Graph Representation

The campus is represented as a weighted graph.

- Nodes represent campus locations.
- Edges represent connections between locations.
- Edge weights represent the sample travel costs between connected locations.

### 5.2 Search Algorithms

**Breadth-First Search (BFS)**

BFS explores the graph level by level and finds a path with the minimum number of edges in an unweighted search.

**Uniform Cost Search (UCS)**

UCS expands the node with the lowest accumulated path cost and finds a minimum-cost path when edge costs are non-negative.

**A* Search**

A* combines the accumulated path cost and a heuristic estimate to guide its search towards the destination.

### 5.3 Time-Aware Navigation

The application supports two modes:

- **Normal Time:** Uses the normal sample edge costs.
- **Lunch Time:** Applies simulated crowd penalties to selected connections.

This demonstrates how changing travel conditions can influence route selection.

## 6. Application Features

1. **Location Selection:** Select starting and destination locations.
2. **Time Mode Selection:** Switch between Normal Time and Lunch Time.
3. **Route Comparison:** View BFS, UCS and A* results together.
4. **Route Details:** View the selected path and its total cost.
5. **Performance Comparison:** Compare distance/cost, nodes explored and execution time.
6. **Route Highlighting:** Highlight the selected path on the campus graph.
7. **Campus Graph Visualization:** View campus nodes and their connections.
8. **Directional Edge Costs:** Display forward and reverse connection costs.

## 7. Installation and Execution

### Prerequisites

- Python installed
- Visual Studio Code
- Live Server extension in VS Code

### Step 1: Open the project

Open the `Smart-Campus-Navigator` folder in VS Code.

### Step 2: Install dependencies

Open the VS Code terminal and execute:

```bash
pip install flask flask-cors
```

### Step 3: Start the backend server

From the project root directory, run:

```bash
python backend/app.py
```

The Flask server runs at:

```text
http://127.0.0.1:5000
```

### Step 4: Start the frontend

1. Open the `frontend` folder.
2. Right-click `index.html`.
3. Select **Open with Live Server**.
4. The Smart Campus Navigator interface opens in your browser.

**Note:** Keep the Flask server running while using the frontend.

## 8. API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/api/locations` | GET | Returns available campus locations |
| `/api/graph` | GET | Returns graph nodes and edges |
| `/api/route` | POST | Calculates and compares routes using all three algorithms |

### Route API Request Example

```json
{
    "start": "Admin Block",
    "destination": "Medical Center",
    "is_lunch_time": true
}
```

The response contains the selected locations, time mode, and results from BFS, UCS and A*.

Each algorithm result includes:

- Path
- Distance / route cost
- Nodes explored
- Execution time

## 9. Performance Evaluation

The application compares the algorithms using three metrics:

| Metric | Description |
|---|---|
| Route Cost | Total accumulated edge cost of the selected path |
| Nodes Explored | Number of nodes explored by the algorithm |
| Execution Time | Time taken by the algorithm, measured in milliseconds |

The comparison charts help understand how the algorithms behave on the same campus graph.

**Note:** BFS prioritizes the minimum number of edges, whereas UCS and A* prioritize minimum accumulated path cost. Therefore, their routes may differ.

Execution times can vary between runs depending on system conditions and graph size.

## 10. Testing

The following scenarios are considered during testing:

- Finding routes between different campus locations.
- Comparing BFS, UCS and A* results.
- Switching between Normal Time and Lunch Time.
- Checking route highlighting on the graph.
- Verifying performance comparison charts.
- Checking API responses.
- Testing identical start and destination locations.
- Checking invalid or missing location inputs.

Algorithm tests are maintained in:

```text
tests/test_algorithms.py
```

## 11. Limitations

- Campus graph values are illustrative sample values, not verified real-world campus measurements.
- Crowd penalties are simulated and do not use live crowd data.
- The current prototype does not use GPS-based live positioning.
- Performance results depend on the graph size and execution environment.

## 12. Future Enhancements

- Integrate actual campus map data.
- Add GPS-based current location support.
- Use real-time crowd information.
- Improve route visualization.
- Extend navigation to additional campus locations.

## 13. Conclusion

Smart Campus Navigator demonstrates how BFS, UCS and A* search algorithms can be applied to campus route planning.

By combining graph representation, time-aware cost adjustments, algorithm comparison and interactive visualization, the project provides a working prototype for understanding intelligent route planning.

---

**Project:** Smart Campus Navigator  
**Domain:** Artificial Intelligence  
**Algorithms:** BFS, UCS and A* Search  