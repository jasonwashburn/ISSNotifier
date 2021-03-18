import requests
from datetime import datetime

MY_LAT = 41.151058 # Your latitude
MY_LONG = -95.900253 # Your longitude


def iss_within_five_deg(lat, long):
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    lat_diff = abs(iss_latitude - lat)
    long_diff = abs(iss_longitude - long)
    if lat_diff <= 5 and long_diff <= 5:
        return True
    else:
        return False


def is_dark(lat, long):
    parameters = {
        "lat": lat,
        "lng": long,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    astro_twilight_end_utc = int(data["results"]["astronomical_twilight_end"].split("T")[1].split(":")[0])
    sunrise_hour_utc = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    astro_twilight_begin_utc = int(data["results"]["astronomical_twilight_begin"].split("T")[1].split(":")[0])
    sunset_hour_utc = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now_utc = datetime.utcnow()

    if astro_twilight_end_utc <= time_now_utc.hour <= astro_twilight_begin_utc:
        return True
    else:
        return False


print(f"ISS Within 5 degrees lat or long? {iss_within_five_deg(lat=MY_LAT, long=MY_LONG)}")
print(f"Is dark outside? {is_dark(lat=MY_LAT, long=MY_LONG)}")
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



