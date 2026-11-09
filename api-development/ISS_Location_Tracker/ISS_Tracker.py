from socketserver import DatagramRequestHandler
from urllib.error import HTTPError
from math import radians, sin, cos, asin, sqrt
import requests
from datetime import datetime
import os
from dotenv import load_dotenv


def main():
    try:
        while True:
            user_choice=input("Near  which city , you want to check ISS Location? : ")
            if user_choice.strip()=="":
                print("You have not given city name")
                continue

            # my current location
            lat_long=get_lat_long(user_choice)

            my_lat=lat_long['my_lat']
            my_long=lat_long['my_long']

            compare_location_dis(my_lat, my_long)

            user_choice = input("Do you want to check location of ISS near any other city? Y/N : ")
            if user_choice.strip().upper() == "N":
                break

    except HTTPError as err:
        print(err)




def get_lat_long(city):
    load_dotenv()

    API_KEY =os.getenv("OPENWEATHER_API_KEY")

    parameter = {
        "q": city,
        "appid": API_KEY
    }
    BASE_URL = "http://api.openweathermap.org/geo/1.0/direct"

    data=requests.get(BASE_URL,parameter).json()

    return {"my_lat":data[0]['lat'], "my_long": data[0]["lon"]}

def get_sunrise_sunset(lat,long):
    BASE_URL = "https://api.sunrise-sunset.org/v2"
    parameters = {
        "lat": lat,
        "long": long
    }

    data=requests.get(BASE_URL,parameters).json()
    sunset_dt=datetime.fromisoformat(data["sunset"])
    sunrise_dt=datetime.fromisoformat(data["sunrise"])
    return {"sunrise":sunrise_dt,"sunset":sunset_dt}


def iss_location_near(my_lat,my_lon):
    #Get International Space Station Location
    BASE_URL = "http://api.open-notify.org/iss-now.json"
    response = requests.get(BASE_URL)
    iss_long = response.json()['iss_position']['longitude']
    iss_lat = response.json()['iss_position']['latitude']

    #calculate distance
    my_lat, my_lon, iss_lat, iss_long = map(radians, [float(my_lat), float(my_lon), float(iss_lat), float(iss_long)])

    # Haversine formula
    dlat = iss_lat - my_lat
    dlon = iss_long - my_lon

    a = sin(dlat / 2) ** 2 + cos(my_lat) * cos(iss_lat) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))

    return 6371 * c  # Distance in kilometres


def compare_location_dis(my_lat, my_lon):
    # my sunset and sunrise time
    my_ss = get_sunrise_sunset(my_lat, my_lon)

    sunset_result = my_ss["sunset"]
    sunrise_result = my_ss["sunrise"]

    #location of ISS near
    d = iss_location_near(my_lat, my_lon)
    if abs(d)<=5:
        # check if sunset happened and there is dark
        if sunrise_result.date() == datetime.now().date() and datetime.now().time() > sunrise_result.time():
            print(f"ISS is in your sky in {abs(d)} Kms and it is dark. Please have a look")
        else:
            print(f"ISS is in your sky in {abs(d)} Kms and it is sunny. You can not see it.")
    else:
        print(f"ISS is in faaar away from you at {round(abs(d),2)} Kms")


if __name__=="__main__":
    main()