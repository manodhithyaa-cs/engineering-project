import network
import urequests
import time
from machine import Pin, ADC

# Configuration
WIFI_SSID = 'your_SSID'
WIFI_PASSWORD = 'your_PASSWORD'
SERVER_URL = 'http://192.168.1.100:80'  # Replace with your local server's IP

# Pin setup
soil_sensor = ADC(Pin(34))  # Analog pin for soil moisture sensor
soil_sensor.atten(ADC.ATTN_11DB)  # Set attenuation to read full range (0-3.3V)
buzzer = Pin(27, Pin.OUT)  # Digital pin for buzzer

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)
    print("Connecting to Wi-Fi...")
    
    # Timeout after 10 seconds if connection is not established
    timeout = 10
    while not wlan.isconnected() and timeout > 0:
        time.sleep(0.5)
        timeout -= 1
        print(".", end="")
    
    if wlan.isconnected():
        print("\nConnected to Wi-Fi")
        print("Network config:", wlan.ifconfig())
    else:
        print("\nFailed to connect to Wi-Fi")
        raise Exception("Wi-Fi connection failed")

def get_soil_moisture():
    readings = []
    for _ in range(5):  # Take 5 readings for averaging
        readings.append(soil_sensor.read())
        time.sleep(0.1)
    average_reading = sum(readings) / len(readings)
    moisture_percent = (4095 - average_reading) / 4095 * 100  # Map to percentage
    return moisture_percent

def send_data(moisture_percent):
    retries = 3
    while retries > 0:
        try:
            response = urequests.post(SERVER_URL, json={"moisture": moisture_percent})
            print("Data sent. Response code:", response.status_code)
            response.close()
            return
        except Exception as e:
            print(f"Failed to send data. Retries left: {retries} - Error: {e}")
            retries -= 1
            time.sleep(2)  # Wait before retrying
    print("Failed to send data after retries.")

def main():
    connect_wifi()
    
    while True:
        moisture_percent = get_soil_moisture()
        print("Soil Moisture: {:.2f}%".format(moisture_percent))

        if moisture_percent < 30:
            buzzer.on()  # Turn on buzzer
            print("Moisture low! Buzzer ON")
        else:
            buzzer.off()  # Turn off buzzer
            print("Moisture level sufficient. Buzzer OFF")
        
        # Send data to server
        send_data(moisture_percent)
        
        time.sleep(5)  # Wait 5 seconds before next reading

# Run main function
main()
