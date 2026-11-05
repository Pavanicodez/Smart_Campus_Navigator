const API_URL = "https://smart-campus-backend-39ao.onrender.com";

const startSelect = document.getElementById("start");
const destinationSelect = document.getElementById("destination");
const timeModeSelect = document.getElementById("timeMode");

const findButton = document.getElementById("findRoute");
const resultDiv = document.getElementById("result");

async function loadLocations() {
    try {
        const response = await fetch(`${API_URL}/api/locations`);

        if (!response.ok) {
            throw new Error("Unable to fetch campus locations");
        }

        const locations = await response.json();

        locations.forEach(location => {
            startSelect.add(new Option(location, location));
            destinationSelect.add(new Option(location, location));
        });

    } catch (error) {
        resultDiv.innerHTML =
            `<p class="error-message">${error.message}. Check Flask server.</p>`;
        console.error(error);
    }
}


// Create a comparison chart using SVG
function createChart(title, metric, results, unit = "") {

    const validResults = Object.entries(results)
        .filter(([algorithm, result]) => result !== null);

    if (validResults.length === 0) {
        return "";
    }

    const values = validResults.map(([algorithm, result]) => ({
        algorithm,
        value: Number(result[metric]) || 0
    }));

    const maxValue = Math.max(...values.map(item => item.value), 1);

    const bars = values.map(item => {

        const barWidth = (item.value / maxValue) * 100;

        return `
            <div class="chart-row">
                <span class="chart-label">${item.algorithm}</span>

                <div class="chart-track">
                    <div class="chart-bar" style="width:${barWidth}%"></div>
                </div>

                <span class="chart-value">
                    ${item.value.toFixed(3)} ${unit}
                </span>
            </div>
        `;
    }).join("");

    return `
        <div class="chart-card">
            <h4>${title}</h4>
            ${bars}
        </div>
    `;
}


// Display performance charts
function displayCharts(results) {

    return `
        <section class="performance-section">

            <h3>Algorithm Performance Comparison</h3>

            <div class="charts-container">

                ${createChart(
                    "Distance / Cost",
                    "distance",
                    results,
                    "units"
                )}

                ${createChart(
                    "Nodes Explored",
                    "nodes_explored",
                    results
                )}

                ${createChart(
                    "Execution Time",
                    "execution_time",
                    results,
                    "ms"
                )}

            </div>

        </section>
    `;
}


// Display algorithm results
function displayResults(data) {

    const cards = Object.entries(data.results)
        .map(([algorithm, result]) => {

            const isRecommended = algorithm === "UCS";

            if (!result) {
                return `
                    <div class="result-card">
                        <h4>${algorithm}</h4>
                        <p>No route found.</p>
                    </div>
                `;
            }

            return `
                <div class="result-card ${isRecommended ? "recommended" : ""}">

                    ${isRecommended
                        ? '<span class="recommended-label">Minimum Cost Route</span>'
                        : ""
                    }

                    <h4>${algorithm}</h4>

                    <p class="route-path">
                        <strong>Path:</strong><br>
                        ${result.path.join(" → ")}
                    </p>

                    <p class="cost">
                        Distance: ${result.distance}
                    </p>

                    <p class="nodes">
                        Nodes Explored: ${result.nodes_explored}
                    </p>

                    <p class="execution">
                        Execution Time: ${result.execution_time} ms
                    </p>

                    <button
                        class="show-route-btn"
                        data-algorithm="${algorithm}">
                        Show on Graph
                    </button>

                </div>
            `;

        }).join("");


    resultDiv.innerHTML = `

        <h3>Route Comparison</h3>

        <p><strong>From:</strong> ${data.start}</p>

        <p><strong>To:</strong> ${data.destination}</p>

        <p>
            <strong>Time Mode:</strong>
            ${data.is_lunch_time ? "Lunch Time" : "Normal Time"}
        </p>

        <div class="results-container">
            ${cards}
        </div>

        ${displayCharts(data.results)}
    `;


    // Show selected route on graph
    document.querySelectorAll(".show-route-btn")
        .forEach(button => {

            button.addEventListener("click", () => {

                const algorithm = button.dataset.algorithm;
                const selectedResult = data.results[algorithm];

                if (selectedResult) {

                    window.showRouteOnGraph(
                        selectedResult.path,
                        data.is_lunch_time
                    );

                    document.getElementById("campusGraph")
                        .scrollIntoView({
                            behavior: "smooth",
                            block: "center"
                        });
                }
            });
        });
}


// Find routes
async function findRoute() {

    const start = startSelect.value;
    const destination = destinationSelect.value;

    if (!start || !destination) {
        alert("Please select both locations!");
        return;
    }

    if (start === destination) {
        alert("Select different locations!");
        return;
    }

    findButton.disabled = true;
    findButton.textContent = "Finding Route...";

    resultDiv.innerHTML = "<p>Calculating routes...</p>";

    try {

        const response = await fetch(`${API_URL}/api/route`, {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                start,
                destination,
                is_lunch_time: timeModeSelect.value === "lunch"
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Route request failed");
        }

        displayResults(data);

    } catch (error) {

        resultDiv.innerHTML =
            `<p class="error-message">${error.message}</p>`;

        console.error(error);

    } finally {

        findButton.disabled = false;
        findButton.textContent = "Find Route";
    }
}


findButton.addEventListener("click", findRoute);

loadLocations();