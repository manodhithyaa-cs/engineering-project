#include <WiFi.h>
#include <HTTPClient.h>

// Wi-Fi credentials
const char* ssid = "your_ssid";
const char* password = "your_password";

// Server configuration
const char* serverIP = "your_server_ip";
const int serverPort = 3000;

// Soil moisture sensor pin
const int soilMoisturePin = 34;

// Function to connect to Wi-Fi
void connectWiFi() {
    WiFi.begin(ssid, password);
    Serial.print("Connecting to WiFi...");

    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }

    Serial.println("\nConnected to WiFi");
    Serial.print("IP Address: ");
    Serial.println(WiFi.localIP());
}

// Function to read soil moisture
int getSoilMoisture() {
    int moistureValue = analogRead(soilMoisturePin);
    return moistureValue;
}

// Function to send data to the server
void sendData(int moistureValue, int moisturePercent) {
    if (WiFi.status() == WL_CONNECTED) {
        HTTPClient http;
        String url = String("http://") + serverIP + ":" + String(serverPort) + "/";
        
        http.begin(url);
        http.addHeader("Content-Type", "application/json");

        // Create JSON payload
        String payload = "{\"moisture_value\": " + String(moistureValue) + 
                         ", \"moisture_percent\": " + String(moisturePercent) + "}";

        // Send HTTP POST request
        int httpResponseCode = http.POST(payload);
        
        if (httpResponseCode > 0) {
            Serial.println("Data sent: " + payload);
        } else {
            Serial.println("Error on sending POST: " + String(httpResponseCode));
        }

        // Close the connection
        http.end();
    } else {
        Serial.println("WiFi not connected");
    }
}

void setup() {
    Serial.begin(115200);
    connectWiFi();
}

void loop() {
    int moistureValue = getSoilMoisture();
    int moisturePercent = (moistureValue * 100) / 1023;

    sendData(moistureValue, moisturePercent);

    delay(10000); // Delay for 10 seconds
}
