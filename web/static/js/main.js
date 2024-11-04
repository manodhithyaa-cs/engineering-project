const pump_status = document.getElementById("pump_status")
const save_btn = document.getElementById("save_btn")
const project_details = document.getElementById("project_details")

project_details.addEventListener("click", () => window.location.href=`/project_details`)

save_btn.addEventListener("click", () => {
    $.post("/", { pump_status: pump_status.value }, (data, status, xhr) => {
        if (data) {
            console.log(data)
            console.log(status)
        } else {
            alert("Error Occurred")
        }
    })
})
