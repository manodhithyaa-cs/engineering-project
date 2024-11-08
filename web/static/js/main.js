const pump_status = document.getElementById("pump_status")
const save_btn = document.getElementById("save_btn")
const project_details = document.getElementById("project_details")

project_details.addEventListener("click", () => window.location.href=`/project_details`)

save_btn.addEventListener("click", () => {
    $.post("/", { pump_status: pump_status.value }, (data, status, xhr) => {
        if (data) {
            console.log(data.status)
            console.log(data.pump_status)
            console.log(status)
        } else {
            alert("Error Occurred")
        }
    })
})

const ctx1 = document.getElementById("chart-1")

new Chart(ctx1, {
    type: "bar",
    data: {
        labels: ["12:00", "12:30", "13:00"],
        datasets: [{
            label: "Moisture Content Percent (Today)",
            data: [60, 70, 80],
            borderWidth: 1
        }]
    }, options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
})

const ctx2 = document.getElementById("chart-2")

new Chart(ctx2, {
    type: "doughnut",
    data: {
        labels: ["ON", "OFF"],
        datasets: [{
            label: "Water Pump",
            data: [11, 16],
            backgroundColor: ["rgb(75, 192, 192)", "rgb(255, 99, 132)"]
        }]
    }, options: {}
})

const ctx3 = document.getElementById("chart-3")

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
    }, options: {}
})