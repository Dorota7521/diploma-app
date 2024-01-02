document.addEventListener("DOMContentLoaded", function () {
  var socket = io.connect("http://" + document.domain + ":" + location.port + "/test");

  var initialDataPoints = 10;

  var combinedChart = new Chart(document.getElementById("combined-chart").getContext("2d"), {
    type: "line",
    data: {
      labels: Array.from({ length: initialDataPoints }, (_, i) => i + 1),
      datasets: [
        {
          label: "CPU Usage",
          data: Array(initialDataPoints).fill(0),
          borderColor: "#3498db", // Blue
          borderWidth: 2,
          fill: false,
        },
        {
          label: "RAM Usage",
          data: Array(initialDataPoints).fill(0),
          borderColor: "#e74c3c", // Red
          borderWidth: 2,
          fill: false,
        },
        {
          label: "Disk Usage",
          data: Array(initialDataPoints).fill(0),
          borderColor: "#8e44ad", // Purple
          borderWidth: 2,
          fill: false,
        },
      ],
    },
    options: {
      scales: {
        x: {
          type: "linear",
          position: "bottom",
          title: {
            display: true,
            text: "Time (seconds)",
          },
        },
        y: {
          beginAtZero: true,
          max: 100,
          title: {
            display: true,
            text: "Usage (%)",
          },
        },
      },
    },
  });

  var updateChart = function (data) {
    combinedChart.data.labels.push(combinedChart.data.labels.length + 1);

    combinedChart.data.datasets[0].data.push(data.cpu);
    combinedChart.data.datasets[1].data.push(data.ram);
    combinedChart.data.datasets[2].data.push(data.disk);

    combinedChart.update();

    // Read min and max values from the chart
    var minValues = combinedChart.data.datasets.map(dataset => Math.min(...dataset.data));
    var maxValues = combinedChart.data.datasets.map(dataset => Math.max(...dataset.data));

    // Calculate differences
    var diffs = maxValues.map((max, i) => max - minValues[i]);

    // Display differences next to the charts
    document.getElementById("cpu-diff").innerText = "CPU usage increased by: " + `${diffs[0].toFixed(2)}` + "%";
    document.getElementById("ram-diff").innerText = "RAM usage increased by: " + `${diffs[1].toFixed(2)}%`, + "%";
    document.getElementById("disk-diff").innerText = "Disk usage increased by " + `${diffs[2].toFixed(2)}` + "%";
  };
  socket.on("update_progress", updateChart);
});
