# ISS Location Tracker 🌍

A simple Python project that checks the current location of the International Space Station (ISS) and calculates its distance from a user-specified city.

### Features
- Get city latitude and longitude using OpenWeatherMap API.
- Retrieve the current ISS location using the Open Notify API.
- Calculate geographical distance using the Haversine formula.
- Retrieve sunrise and sunset times.
- Display the approximate ISS distance from the selected city.

### Technologies
- Python
- Requests
- REST APIs
- Math module
- Datetime module

### How to Run

1. Install dependencies:
   ```bash
   pip install requests
   ```
2. Configure your OpenWeatherMap API key.
3. Run the program:
   ```bash
   python main.py
   ```
4. Enter a city name to check the ISS location.

### Learning Outcomes
- Working with REST APIs and JSON responses.
- Handling API data and type conversions.
- Implementing the Haversine distance formula.
- Using Python functions and exception handling.