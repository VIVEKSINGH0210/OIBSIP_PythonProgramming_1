🌤 Weather App using Python (Tkinter)

📌 Project Overview
This is a simple Weather Application built using Python Tkinter and the OpenWeatherMap API.

The app allows users to enter a city name and instantly get:

🌡 Temperature (in Celsius)

💧 Humidity

🌬 Wind Speed

☁ Weather Condition

It provides real-time weather data with a clean and simple graphical user interface (GUI).

🛠 Technologies Used
Python

Tkinter (for GUI)

Requests library (for API calls)

OpenWeatherMap API


🚀 How It Works
User enters the city name.

The app sends a request to OpenWeatherMap API.

Weather data is fetched in JSON format.

Temperature is converted from Kelvin to Celsius.

Weather details are displayed in the application window.

💻 Installation & Setup
Step 1: Install Required Library
Bash

pip install requests
Step 2: Run the Application
Bash

python weather.py
(Replace weather.py with your file name if different.)

🔑 API Key
This project uses OpenWeatherMap API.

To use your own API key:

Create an account at https://openweathermap.org

Generate your API key

Replace this line in the code:

Python

api_key = "your_api_key_here"

🎯 Features
Simple and user-friendly interface

Real-time weather data

Error handling for invalid city names

Clean formatted output display

📷 Sample Output
When a valid city name is entered:

Code

🌤 Weather in Kolkata

Temperature: 29.4 °C


Humidity   : 78%


Wind Speed : 3.5 m/s


Condition  : light rain


📌 Future Improvements
Add weather icons

Add background images

Add temperature unit toggle (°C / °F)

Improve UI design

Hide API key using environment variables

👨‍💻 Author

Vivek Kumar


Python Developer | Internship Project
