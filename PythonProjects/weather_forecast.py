# Prerequisites: Install request module using pip
 
import requests

def get_weather_report(api_key, city):
    url = f"http://api.weatherapi.com/v1/current.json?q={city}&key={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if data["location"]:
        location = data["location"]["name"]
        weather_description = data["current"]["condition"]['text'].upper()
        temperature = data["current"]["temp_c"]
        feels_like = data["current"]["feelslike_c"]
        humidity = data["current"]["humidity"]
        wind_speed = data["current"]["wind_mph"]

        report = f"Weather in {location}: {weather_description}\nTemperature: {temperature}°C\nFeels like: {feels_like}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} kph"
        
        return report
    else:
        return f"Error: {data['error']}"

if __name__ == "__main__":
    api_key = 'your_api_key'  # Replace 'your_api_key' with your OpenWeatherMap API key
    city = input('Enter City/Postal Code: ') # Get weather by user input
    # city = 'auto:ip' # Get weather by user's current location

    weather_report = get_weather_report(api_key, city)
    print(weather_report)
