import tkinter as tk
import requests
def fetch_weather():
    city=city_entry.get()
    api_key="5aa381ba09dc12c8c10d80d3f8f540cc"
    if city=="":
        result_label.config(text="Please enter city name")
        return
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    try:
        data=requests.get(url).json()
        if data["cod"]!=200:
            result_label.config(text="City not found")
            return
        temp=data["main"]["temp"]-273.15
        humidity=data["main"]["humidity"]
        wind=data["wind"]["speed"]
        condition=data["weather"][0]["description"]
        result_label.config(
            text=f"🌤 Weather in {city}\n\n"
                 f"Temperature: {temp} °C\n"
                 f"Humidity   : {humidity}%\n"
                 f"Wind Speed : {wind} m/s\n"
                 f"Condition  : {condition}"
        )

    except:
        result_label.config(text="Error fetching data")
app=tk.Tk()
app.title("Weather App")
app.geometry("350x300")
tk.Label(app,text="Enter City Name",font=("Rubik", 12)).pack(pady=5)
city_entry=tk.Entry(app,width=25)
city_entry.pack()
tk.Button(app,text="Get Weather",command=fetch_weather).pack(pady=10)
result_label=tk.Label(app,text="",font=("Rubik", 11),justify="left")
result_label.pack(pady=10)
app.mainloop()
