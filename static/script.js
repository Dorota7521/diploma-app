// static/script.js

document.addEventListener("DOMContentLoaded", function () {
  var socket = io.connect("http://" + document.domain + ":" + location.port + "/test");

  var initialDataPoints = 20;

  var cpuChart = new Chart(document.getElementById("cpu-chart").getContext("2d"), {
    type: "line",
    data: {
      labels: Array.from({ length: initialDataPoints }, (_, i) => i + 1),
      datasets: [
        {
          label: "CPU Usage",
          data: Array(initialDataPoints).fill(0),
          borderColor: "#3498db",
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
        },
        y: {
          beginAtZero: true,
          max: 100,
        },
      },
    },
  });

  var ramChart = new Chart(document.getElementById("ram-chart").getContext("2d"), {
    type: "line",
    data: {
      labels: Array.from({ length: initialDataPoints }, (_, i) => i + 1),
      datasets: [
        {
          label: "RAM Usage",
          data: Array(initialDataPoints).fill(0),
          borderColor: "#e74c3c",
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
        },
        y: {
          beginAtZero: true,
          max: 100,
        },
      },
    },
  });

  var diskChart = new Chart(document.getElementById("disk-chart").getContext("2d"), {
    type: "line",
    data: {
      labels: Array.from({ length: initialDataPoints }, (_, i) => i + 1),
      datasets: [
        {
          label: "Disk Usage",
          data: Array(initialDataPoints).fill(0),
          borderColor: "#8e44ad",
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
        },
        y: {
          beginAtZero: true,
          max: 100,
        },
      },
    },
  });

  var updateCharts = function (data) {
    cpuChart.data.labels.push(cpuChart.data.labels.length + 1);
    ramChart.data.labels.push(ramChart.data.labels.length + 1);
    diskChart.data.labels.push(diskChart.data.labels.length + 1);

    cpuChart.data.datasets[0].data.push(data.cpu);
    ramChart.data.datasets[0].data.push(data.ram);
    diskChart.data.datasets[0].data.push(data.disk);

    // Limit the number of data points displayed to 20 for better performance
    var maxDataPoints = 100;
    if (cpuChart.data.labels.length > maxDataPoints) {
      cpuChart.data.labels.shift();
      ramChart.data.labels.shift();
      diskChart.data.labels.shift();
      cpuChart.data.datasets[0].data.shift();
      ramChart.data.datasets[0].data.shift();
      diskChart.data.datasets[0].data.shift();
    }

    cpuChart.update();
    ramChart.update();
    diskChart.update();
  };

  socket.on("update_progress", updateCharts);
  console.log("%c❤️ Kocham moją przyszłą żonę!", "color: red; font-size: 24px;");
});
