import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
USR_NAME = os.environ["MY_USR_NAME"]
USR_PASS = os.environ["MY_PASS"]
TOKEN = os.environ["MY_TOKEN_BASIC"]

USER_ID = os.environ["MY_USR_ID"]

AUTH_TYPE = "Basic"
SHEETY_PRICES_ENDPOINT = os.environ["SHEETY_PRICES_ENDPOINT"]
SHEETY_USERS_ENDPOINT = os.environ["SHEETY_USERS_ENDPOINT"]

MY_SMTP_SID = os.environ["MY_SMTP_SID"]
MY_SMTP_AUTH_TOKEN = os.environ["MY_SMTP_AUTH_TOKEN"]
MY_EMAIL = os.environ["MY_EMAIL"]
MY_APP_PASSWORD = os.environ["MY_APP_PASSWORD"]


class DataManager:

    def __init__(self):
        self._user = USR_NAME
        self._password = USR_PASS
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self._prices_endpoint = SHEETY_PRICES_ENDPOINT
        self._users_endpoint = SHEETY_PRICES_ENDPOINT
        self._smtp_sid = MY_SMTP_SID
        self._smtp_token = MY_SMTP_AUTH_TOKEN
        self._email = MY_EMAIL
        self._app_password = MY_APP_PASSWORD
        self.user_data = {}      
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=self._prices_endpoint, auth=self._authorization)
        data = response.json()
        print(data)
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", 
                json=new_data, 
                auth=self._authorization
            )
            print(response.text)
    
    def get_customer_emails(self):
        response = requests.get(url=self._users_endpoint, auth=self._authorization)
        data = response.json()
        self.user_data = data["users"]
        return self.user_data

