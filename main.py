import os
import requests
import matplotlib.pyplot as plt
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Create images folder (VERY IMPORTANT FIX)
IMAGE_FOLDER = "images"
os.makedirs(IMAGE_FOLDER, exist_ok=True)

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error fetching data:", response.json())
        return None
    
    return response.json()

def save_weather_chart(data, city):
    # Extract data
    times = []
    temps = []

    for item in data["list"][:10]:  # first few entries
        times.append(item["dt_txt"])
        temps.append(item["main"]["temp"])

    # Plot
    plt.figure(figsize=(10, 5))
    plt.plot(times, temps, marker='o')
    plt.title(f"Temperature Forecast - {city}")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)

    # IMPORTANT: correct file path inside images folder
    file_path = os.path.join(IMAGE_FOLDER, f"{city}_forecast.png")

    plt.tight_layout()
    plt.savefig(file_path)   # SAVE IMAGE HERE
    plt.close()              # VERY IMPORTANT (prevents empty images)

    print(f"Image saved at: {file_path}")

def main():
    city = input("Enter city name: ")
    data = get_weather(city)

    if data:
        save_weather_chart(data, city)

if __name__ == "__main__":
    main()