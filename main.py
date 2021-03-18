import smtplib
import requests
from datetime import datetime
import config

MY_LAT = 41.151058  # Your latitude
MY_LONG = -95.900253  # Your longitude
MY_EMAIL = config.my_email  # Your gmail login email (store in config.py)
PASSWORD = config.password  # Your gmail password (store in config.py)
TARGET_EMAIL = config.target_email  # The email address to sent the notification to


def iss_within_five_deg(lat, long):
    """
    Checks to see if the International Space Station is within 5 degrees of latitude or longitude from the supplied
    position. Uses the open-notify ISS-Location-Now API.
    Documentation: http://open-notify.org/Open-Notify-API/ISS-Location-Now/

    :param lat: The latitude of the location to check
    :param long: The longitude of the location to check
    :return: Boolean
    """
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
    """
    Checks to see if it is dark (between the ending and beginning of astrological twilight) at the supplied
    position. Uses the sunrise-sunset.org API.
    Documentation: https://sunrise-sunset.org/api

    :param lat: The latitude of the location to check
    :param long: The longitude of the location to check
    :return: Boolean
    """
    parameters = {
        "lat": lat,
        "lng": long,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    astro_twilight_end_utc = int(data["results"]["astronomical_twilight_end"].split("T")[1].split(":")[0])
    astro_twilight_begin_utc = int(data["results"]["astronomical_twilight_begin"].split("T")[1].split(":")[0])

    time_now_utc = datetime.utcnow()

    if astro_twilight_end_utc <= time_now_utc.hour <= astro_twilight_begin_utc:
        return True
    else:
        return False


def send_email(to_address, subject, message):
    """
    Sends an email message with gmail using the account info provided in config.py

    :param to_address: email address of the recipient
    :param subject: subject of email
    :param message: message to send
    :return: None
    """

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=config.my_email, password=config.password)
        connection.sendmail(
            from_addr=config.my_email,
            to_addrs=to_address,
            msg=f"Subject: {subject}\n\n{message}"
        )


# Build the contents of the notification email
with open('iss_art.txt', 'r') as file:
    iss_ascii = file.read()

iss_message = iss_ascii + "Look Up!\n\nThe International Space Station is Overhead."

# Check to see if the ISS is overhead and whether its dark. If so, send an email
if iss_within_five_deg(lat=MY_LAT, long=MY_LONG) & is_dark(lat=MY_LAT, long=MY_LONG):
    send_email(to_address=TARGET_EMAIL, subject="ISS Overhead!", message=iss_message)
