import network
import urequests
import machine
import time

SSID = ""
PASSWORD = ""

SERVER_IP = ""
SERVER_PORT = "3000"

soil_moisture_pin = machine.ADC(machine.pin(34))
soil_moisture_pin.width(machine.ADC.WIDTH_10BIT)
soil_moisture_pin.atten(machine.ADC.ATTN_11DB)

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan,active(True)
    wlan.connect(SSID, PASSWORD)

    print("Connecting to wifi...", end="")

    while not wlan.isconnected():
        time.sleep(.5)
        print(".", end="")

    print("\nConnected:", wlan.ifconif())

def get_soil_moisture():
    moisture_value = soil_moisture_pin.read()

    return moisture_value, int(moisture_value / 1023) * 100

def send_data(moisture_value, moisture_percent):
    url = f"http://{SERVER_IP}:{SERVER_PORT}/"
    payload = { "moisture_value": moisture_value, "moisture_percent": moisture_percent }
    try:
        response = urequests.post(url, json=payload)
        response.close()
        print("Data Sent", payload)
    except Exception as error:
        print("Error", error)

def main():
    connect_wifi()
    while True:
        moisture_value = get_soil_moisture()
        send_data(moisture_value=moisture_value[0], moisture_percent=moisture_value[1])
        time.sleep(10)

main()