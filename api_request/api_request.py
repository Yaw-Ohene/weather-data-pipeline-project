import requests
api_key = "282661ccc0f44c9b0fc1b47254d1dad4"
api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query=New York"

# def fetch_data():
#     print("Fetching data from Weatherstack API...")
#     try:

#         response = requests.get(api_url)
#         response.raise_for_status()
#         print("API request successful.")
#         return response.json()
    
#     except requests.exceptions.RequestException as e:
#         print(f"An error occurred: {e}")
#         raise

# fetch_data()

def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2025-09-22 19:31', 'localtime_epoch': 1758569460, 'utc_offset': '-4.0'}, 'current': {'observation_time': '11:31 PM', 'temperature': 19, 'weather_code': 113, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0008_clear_sky_night.png'], 'weather_descriptions': ['Clear '], 'astro': {'sunrise': '06:44 AM', 'sunset': '06:53 PM', 'moonrise': '07:29 AM', 'moonset': '07:07 PM', 'moon_phase': 'Waxing Crescent', 'moon_illumination': 0}, 'air_quality': {'co': '384.8', 'no2': '85.1', 'o3': '42', 'so2': '13.69', 'pm2_5': '27.195', 'pm10': '29.23', 'us-epa-index': '2', 'gb-defra-index': '2'}, 'wind_speed': 18, 'wind_degree': 163, 'wind_dir': 'SSE', 'pressure': 1018, 'precip': 0, 'humidity': 73, 'cloudcover': 0, 'feelslike': 19, 'uv_index': 0, 'visibility': 16, 'is_day': 'no'}}