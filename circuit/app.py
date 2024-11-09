import network
import time
from machine import Pin, ADC
import urequests
import socket
import struct
import BlynkLib  # Make sure the Blynk library is available

# Configuration
WIFI_SSID = 'your_SSID'
WIFI_PASSWORD = 'your_PASSWORD'
BLYNK_AUTH_TOKEN = 'your_BLYNK_AUTH_TOKEN'  # Replace with your Blynk Auth Token

# Pin setup
soil_sensor = ADC(Pin(34))  # Analog pin for soil moisture sensor
soil_sensor.atten(ADC.ATTN_11DB)  # Set attenuation to read full range (0-3.3V)
buzzer = Pin(27, Pin.OUT)  # Digital pin for buzzer

# Set up Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH_TOKEN)

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

def send_to_blynk(moisture_percent):
    # Sending soil moisture value to Blynk virtual pin (V1)
    blynk.virtual_write(1, moisture_percent)

    # If moisture is low, send buzzer status to V2 (0 = OFF, 1 = ON)
    if moisture_percent < 30:
        buzzer.on()
        print("Moisture low! Buzzer ON")
        blynk.virtual_write(2, 1)  # Set virtual pin V2 (buzzer) to ON
    else:
        buzzer.off()
        print("Moisture level sufficient. Buzzer OFF")
        blynk.virtual_write(2, 0)  # Set virtual pin V2 (buzzer) to OFF

def main():
    connect_wifi()
    
    while True:
        moisture_percent = get_soil_moisture()
        print("Soil Moisture: {:.2f}%".format(moisture_percent))

        # Send soil moisture data to Blynk
        send_to_blynk(moisture_percent)
        
        # Run Blynk loop to handle communication
        blynk.run()
        
        time.sleep(5)  # Wait 5 seconds before next reading

# Run main function
main()
