<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" >
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
        <link href="index.css" rel="stylesheet" />
        <title>Engineering Project</title>
    </head>
    <body>
        <main class="container">
            <nav class="navbar bg-body-tertiary">
                <div class="container-fluid">
                  <a class="navbar-brand d-flex w-100" style="justify-content: space-between;" href="#">
                    <img src="logo.png" alt="Logo" class="d-inline-block align-text-top">
                    <span style="margin-top: auto; margin-bottom: auto;">
                        Engineering Project
                        <br />
                        <button class="btn btn-outline-primary" id="project_details">VIEW PROJECT DETAILS</button>
                    </span>
                  </a>
                </div>
            </nav>

            <div class="row mb-5">
                <div class="col-lg-4 col-sm-12 card">
                    <canvas id="chart-1"></canvas>
                </div>
                <div class="col-lg-4 col-sm-12 card">  
                    <canvas id="chart-2"></canvas>
                </div>
                <div class="col-lg-4 col-sm-12 card">
                    <canvas id="chart-3"></canvas>
                </div>
            </div>

            <table class="table table-striped">
                <thead>
                    <th style="padding: 1rem;">#</th>
                    <th style="padding: 1rem;">Time</th>
                    <th style="padding: 1rem;">Moisture content</th>
                    <th style="padding: 1rem;">Water Pump Status</th>
                </thead>
                <tbody>
                    <!-- <tr>
                        <td style="padding: 1rem;" colspan="3">
                            <span>Pump Status: </span>
                            <select name="pump_status" id="pump_status">
                                <option value="ON">ON</option>
                                <option value="OFF">OFF</option>
                            </select>
                        </td>
                        <td style="padding: 1rem;" colspan="1">
                            <button type="button" id="save_btn" class="btn btn-primary w-100">Save</button>
                        </td>
                    </tr> -->
                </tbody>
            </table>
        </main>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <script src="main.js"></script>
    </body>
</html>