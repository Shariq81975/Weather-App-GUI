import tkinter as tk
import requests

# function to get weather data from API
def get_weather_data(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    
    if response.status_code != 200:
        # handle API request error
        raise Exception("Error: API request failed")
    
    data = response.json()
    return data

# function to display weather data in GUI
def show_weather_data(data):
    city_name = data['name']
    temp_kelvin = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    
    # convert temperature from Kelvin to Celsius
    temp_celsius = round(temp_kelvin - 273.15, 2)
    
    # create weather data display string
    display_str = f"City: {city_name}\nTemperature: {temp_celsius} °C\nHumidity: {humidity}%\nWind speed: {wind_speed} m/s"
    
    # display weather data in GUI
    result_label.config(text=display_str)

# function to handle button click
def button_click():
    city = city_entry.get()
    
    try:
        data = get_weather_data(api_key, city)
        show_weather_data(data)
    except Exception as e:
        result_label.config(text=str(e))

# initialize GUI window
window = tk.Tk()
window.title("Weather App")
window.geometry("400x300")
window.resizable(False, False)

# add background image
bg_image = tk.PhotoImage(file="background.png")
bg_label = tk.Label(window, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# add title label
title_label = tk.Label(window, text="Weather App", font=("Helvetica", 20, "bold"), fg="white", bg="#0077be")
title_label.pack(fill="x")

# add city input label and entry box
city_label = tk.Label(window, text="Enter a city name:", font=("Helvetica", 14), fg="white", bg="#0077be")
city_label.place(relx=0.2, rely=0.3, anchor="center")
city_entry = tk.Entry(window, font=("Helvetica", 14))
city_entry.place(relx=0.5, rely=0.3, anchor="center")

# add search button
search_button = tk.Button(window, text="Search", font=("Helvetica", 14), bg="#0077be", fg="white", command=button_click)
search_button.place(relx=0.5, rely=0.4, anchor="center")

# add result label
result_label = tk.Label(window, font=("Helvetica", 14), fg="white", bg="#0077be", justify="left")
result_label.place(relx=0.5, rely=0.6, anchor="center")

# run GUI main loop
window.mainloop()
