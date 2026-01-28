import requests
api_key="494e662c393d6879785d7e0c636809c6"
api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query=New York"
def fetch_data():
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        print("Data fetched successfully")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        raise


def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2026-01-07 04:41', 'localtime_epoch': 1767760860, 'utc_offset': '-5.0'}, 'current': {'observation_time': '09:41 AM', 'temperature': 3, 'weather_code': 143, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0006_mist.png'], 'weather_descriptions': ['Mist'], 'astro': {'sunrise': '07:20 AM', 'sunset': '04:45 PM', 'moonrise': '09:50 PM', 'moonset': '10:04 AM', 'moon_phase': 'Waning Gibbous', 'moon_illumination': 84}, 'air_quality': {'co': '349.85', 'no2': '34.45', 'o3': '16', 'so2': '10.25', 'pm2_5': '17.95', 'pm10': '18.05', 'us-epa-index': '2', 'gb-defra-index': '2'}, 'wind_speed': 6, 'wind_degree': 247, 'wind_dir': 'WSW', 'pressure': 1004, 'precip': 0.2, 'humidity': 92, 'cloudcover': 60, 'feelslike': 1, 'uv_index': 0, 'visibility': 1, 'is_day': 'no'}}