# 🌦️ Weather Forecast Alert Application

A Python-based Weather Forecast Alert system that fetches real-time weather data using the OpenWeather API and generates visual graphs and structured reports for multiple cities like Mumbai and Bengaluru.

---

## 📌 Project Overview

This project is designed to retrieve live weather information and present it in both visual and structured formats. It demonstrates API integration, data processing, file handling, and data visualization using Python.

✔ Fetches real-time weather data  
✔ Displays temperature, humidity, and weather conditions  
✔ Generates weather forecast graphs  
✔ Stores data in CSV format for analysis  
✔ Supports multiple cities  

---

## 🚀 Features

- 🌍 Real-time weather data using OpenWeather API  
- 📊 Temperature forecast visualization using Matplotlib  
- 📁 Automatic CSV report generation  
- 🏙️ Multi-city support (Mumbai, Bengaluru, etc.)  
- 📂 Organized output folders (`images`, `report`)  
- 🔐 Secure API key handling using `.env`  

---

## 🛠️ Technologies Used

- Python 🐍  
- OpenWeather API 🌐  
- Matplotlib 📊  
- Requests Library 🔗  
- CSV Module 📁  
- Dotenv 🔐  

---

## 📁 PROJECT STRUCTURE

```text
Weather-Forecast-Alert-Application/
│
├── main.py                         → Main Python script that fetches real-time weather data, generates graphs, and updates reports
│
├── .env                            → Stores OpenWeather API key securely for API access
│
├── images/                         → Stores generated weather forecast visualizations (graphs)
│   ├── Mumbai_forecast.png
│   ├── Bengaluru_forecast.png
│
├── report/                         → Stores structured weather reports in CSV format
│   └── weather_report.csv
│
├── requirements.txt                → Contains all required Python dependencies for the project
│
└── README.md                       → Project documentation for GitHub users
