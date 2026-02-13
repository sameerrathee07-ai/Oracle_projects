import requests

API_KEY = "8b68f799170c1eda5152c8c085f8a899"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        return None

    data = response.json()

    weather_info = {
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"]
    }
    return weather_info

def main():
    city = input("Enter city name: ").strip()

    if city == "":
        print("City name cannot be empty")
        return

    weather = get_weather(city)

    if weather is None:
        print("Invalid city name or network error")
        return
    
    print("Temperature:", weather["temperature"], "C")
    print("Feels Like:", weather["feels_like"], "C")
    print("Humidity:", weather["humidity"], "%")
    print("Condition:", weather["description"])

if __name__ == "__main__":
    main()