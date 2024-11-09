const pump_status = document.getElementById("pump_status")
const save_btn = document.getElementById("save_btn")
const project_details = document.getElementById("project_details")

project_details.addEventListener("click", () => window.location.href = `/project_details.php`)

// Get data from microcontroller

const data_moisture = []

setInterval(() => {
    $.get("/get_data", (data, status) => {
        console.log(`Status: ${status}`);
        console.log(`Data from microcontroller: ${data}`);
        data_moisture.push(data)

        const tbody = document.getElementsByClassName("tbody")
        tbody.innerHTML += `<tr>
        <td>${data_moisture.length + 1}</td><td>${data.time}</td><td>${data.moisture_content}</td><td>${data.pump_status}</td></tr>`
    
    })

    console.log("hello")
}, 2000);

// Chart section

const ctx1 = document.getElementById("chart-1");

new Chart(ctx1, {
    type: "bar",
    data: {
        labels: ["12:00", "12:30", "13:00"],
        datasets: [{
            label: "Moisture Content Percent (Today)",
            data: [60, 70, 80],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

const ctx2 = document.getElementById("chart-2");

new Chart(ctx2, {
    type: "doughnut",
    data: {
        labels: ["ON", "OFF"],
        datasets: [{
            label: "Water Pump",
            data: [11, 16],
            backgroundColor: ["rgb(75, 192, 192)", "rgb(255, 99, 132)"]
        }]
    },
    options: {}
});

const ctx3 = document.getElementById("chart-3");

new Chart(ctx3, {
    type: "bubble",
    data: {
        datasets: [{
            label: 'Avg Moisture Percent (This Week)',
            data: [{
                x: 20,
                y: 30,
                r: 15
            }, {
                x: 40,
                y: 10,
                r: 10
            }, {
                x: 30,
                y: 20,
                r: 25
            }, {
                x: 45,
                y: 33,
                r: 15
            }],
            backgroundColor: 'rgb(255, 99, 132)'
        }]
    },
    options: {}
});
