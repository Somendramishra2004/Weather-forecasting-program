import requests

def get_weather(api_key, city):
    base_url = f"http://dataservice.accuweather.com/locations/v1/cities/search"
    params = {'apikey': api_key, 'q': city}

    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        location_data = response.json()
        if location_data:
            location_key = location_data[0]['Key']
            weather_url = f"http://dataservice.accuweather.com/currentconditions/v1/{location_key}"
            weather_params = {'apikey': api_key}
            weather_response = requests.get(weather_url, params=weather_params)

            if weather_response.status_code == 200:
                weather_data = weather_response.json()
                if weather_data:
                    weather_info = weather_data[0]
                    print(f"Weather in {city}: {weather_info['WeatherText']}")
                    print(f"Temperature: {weather_info['Temperature']['Metric']['Value']}°C")
                    print("Full Weather Info:", weather_info)  # Print full weather info
                    
                    if 'RelativeHumidity' in weather_info:
                        print(f"Relative Humidity: {weather_info['RelativeHumidity']}%")
                    else:
                        print("Relative Humidity: Data not available")
                else:
                    print("Weather data not found.")
            else:
                print("Error retrieving weather data.")
        else:
            print("Location not found.")
    else:
        print("Error retrieving location data.")

api_key = 'ZsWU7XZnSf9AbwNzN6pzaLiVtiDlR8Zx'
city_name = input("Enter city name: ")
get_weather(api_key, city_name)
 