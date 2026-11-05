const GRAPH_API = "https://smart-campus-backend-39ao.onrender.com";

const svg = document.getElementById("campusGraph");

const normalButton = document.getElementById("normalGraph");
const lunchButton = document.getElementById("lunchGraph");

let currentNodes = [];
let currentEdges = [];
let currentLunchMode = false;


// Load campus graph
async function loadCampusGraph(isLunchTime = false, selectedPath = null) {

    try {
        const response = await fetch(
            `${GRAPH_API}/api/graph?lunch=${isLunchTime}`
        );

        if (!response.ok) {
            throw new Error("Unable to load campus graph");
        }

        const data = await response.json();

        currentNodes = data.nodes;
        currentEdges = data.edges;
        currentLunchMode = isLunchTime;

        drawGraph(data.nodes, data.edges, selectedPath);

    } catch (error) {
        console.error(error);
        svg.innerHTML = "";
        alert("Unable to load graph. Check Flask server.");
    }
}


// Draw graph and highlight selected route
function drawGraph(nodes, edges, selectedPath = null) {

    const width = 900;
    const height = 600;

    const centerX = width / 2;
    const centerY = height / 2;
    const radius = 220;

    const positions = {};

    // Arrange nodes in circular layout
    nodes.forEach((node, index) => {

        const angle = (2 * Math.PI * index) / nodes.length;

        positions[node] = {
            x: centerX + radius * Math.cos(angle),
            y: centerY + radius * Math.sin(angle)
        };
    });

    svg.setAttribute("viewBox", `0 0 ${width} ${height}`);
    svg.innerHTML = "";

    // Identify selected route connections
    const routeEdges = new Set(selectedPath
        ? selectedPath.slice(0, -1).map((node, index) => {
            const nextNode = selectedPath[index + 1];

            return [node, nextNode].sort().join("|");
        })
        : []
    );

    const routeNodes = new Set(selectedPath || []);

    // Draw connections
    edges.forEach(edge => {

        const start = positions[edge.from];
        const end = positions[edge.to];

        const edgeKey = [edge.from, edge.to].sort().join("|");

        const isSelected = routeEdges.has(edgeKey);

        const line = document.createElementNS(
            "http://www.w3.org/2000/svg",
            "line"
        );

        line.setAttribute("x1", start.x);
        line.setAttribute("y1", start.y);
        line.setAttribute("x2", end.x);
        line.setAttribute("y2", end.y);

        line.setAttribute("stroke", isSelected ? "#f97316" : "#94a3b8");
        line.setAttribute("stroke-width", isSelected ? "5" : "2");

        svg.appendChild(line);

        // Distance label
        const label = document.createElementNS(
            "http://www.w3.org/2000/svg",
            "text"
        );

        label.setAttribute("x", (start.x + end.x) / 2);
        label.setAttribute("y", (start.y + end.y) / 2 - 6);

        label.setAttribute("font-size", "11");
        label.setAttribute("fill", isSelected ? "#ea580c" : "#334155");
        label.setAttribute("text-anchor", "middle");

        const forward = edge.forward_distance ?? "—";
        const reverse = edge.reverse_distance ?? "—";

        label.textContent = `${forward} / ${reverse}`;

        svg.appendChild(label);
    });

    // Draw nodes
    nodes.forEach(node => {

        const position = positions[node];
        const isSelected = routeNodes.has(node);

        const circle = document.createElementNS(
            "http://www.w3.org/2000/svg",
            "circle"
        );

        circle.setAttribute("cx", position.x);
        circle.setAttribute("cy", position.y);
        circle.setAttribute("r", isSelected ? "17" : "13");

        circle.setAttribute(
            "fill",
            isSelected ? "#f97316" : "#2563eb"
        );

        circle.setAttribute("stroke", "white");
        circle.setAttribute("stroke-width", "3");

        svg.appendChild(circle);

        const label = document.createElementNS(
            "http://www.w3.org/2000/svg",
            "text"
        );

        label.setAttribute("x", position.x);
        label.setAttribute("y", position.y + 30);
        label.setAttribute("font-size", "12");
        label.setAttribute("fill", "#173b70");
        label.setAttribute("text-anchor", "middle");
        label.setAttribute("font-weight", "bold");

        label.textContent = node;

        svg.appendChild(label);
    });

    // Show selected algorithm path
    if (selectedPath) {

        const title = document.createElementNS(
            "http://www.w3.org/2000/svg",
            "text"
        );

        title.setAttribute("x", 20);
        title.setAttribute("y", 25);
        title.setAttribute("font-size", "15");
        title.setAttribute("font-weight", "bold");
        title.setAttribute("fill", "#ea580c");

        title.textContent = "Selected Route: " + selectedPath.join(" → ");

        svg.appendChild(title);
    }
}


// Called when user clicks Show on Graph
window.showRouteOnGraph = function(path, isLunchTime) {

    loadCampusGraph(isLunchTime, path);

};


// Normal graph button
normalButton.addEventListener("click", () => {
    loadCampusGraph(false);
});


// Lunch graph button
lunchButton.addEventListener("click", () => {
    loadCampusGraph(true);
});


// Initial graph
loadCampusGraph(false);