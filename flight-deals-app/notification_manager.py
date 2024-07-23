import os
from twilio.rest import Client
from dotenv import load_dotenv
from flight_data import FlightData
from data_manager import DataManager
import smtplib

load_dotenv()

MY_NUM = os.environ.get("MY_PERSONAL_NUMBER", ".env key does not exist for personal number")
MY_VIRTUAL_NUM = os.environ.get("MY_VIRTUAL_NUMBER", ".env key does not exist for virtual number")
MY_SID = os.environ.get("MY_WHATSAPP_SID", ".env key does not exist for SID")
MY_AUTH_TOKEN = os.environ.get("MY_WHATSAPP_AUTH_TOKEN", ".env key does not exist for authorization token")


class NotificationManager:

    def __init__(self, flight_data: FlightData) -> None:
        self.cheapest_price = flight_data.price
        self.origin_code = flight_data.origin_airport
        self.destination_code = flight_data.destination_airport
        self.outbound_date = flight_data.out_date
        self.inbound_date = flight_data.return_date
    
    def send_alert(self):
        client = Client(MY_SID, MY_AUTH_TOKEN)
        message = client.messages.create(
            from_=f"whatsapp:{MY_VIRTUAL_NUM}",
            body=f"LOW PRICE ALERT: For only {self.cheapest_price} 😁\n\n"
                 f"Fly from {self.origin_code} to {self.destination_code} ✈️\n"
                 f"Deal available from {self.outbound_date} to {self.inbound_date}\n\n"
                 f"- Generated from your Flight Deals app and sent via Twilio",
            to=f"whatsapp:{MY_NUM}"
        )

    def send_email(self):
        some_user_data = DataManager()
        customer_data = some_user_data.get_customer_emails()
        for row in customer_data:
            email = row["whatisyouremail?"]
            with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=some_user_data._email, password=some_user_data._password)
                connection.sendmail(
                    from_addr=some_user_data._email,
                    to_addrs=email,
                    msg=f"Subject: LOW PRICE ALERT\n\n"
                        f"Dear {row['whatisyourname?']},\n\n"
                        f"For only {self.cheapest_price} 😁.\n\n"
                        f"Fly from {self.origin_code} to {self.destination_code} ✈️\n"
                        f"Deal available from {self.outbound_date} to {self.inbound_date}\n\n"
                        f"- Generated from your Flight Deals app and sent via SMTP\n\n"
                        f"From\n"
                        f"Gian"
                )