import os
import requests
from dotenv import load_dotenv

amadeus_endpoint = "https://test.api.amadeus.com"
token_endpoint = "/v1/security/oauth2/token"
cities_endpoint = "/v1/reference-data/locations/cities"
offers_endpoint = "/v2/shopping/flight-offers"
get_token = f"{amadeus_endpoint}{token_endpoint}"
get_cities = f"{amadeus_endpoint}{cities_endpoint}"
get_flights = f"{amadeus_endpoint}{offers_endpoint}"

load_dotenv()

CURRENCY = "PHP"


class FlightSearch:

    def __init__(self):
        self._api_key = os.environ["AMADEUS_API_KEY"]
        self._api_secret = os.environ["AMADEUS_API_SECRET"]
        self._token = self._get_new_token()

    def get_destination_code(self, city_name):
        headers_amadeus = {
            "Authorization": f"Bearer {self._token}"
        }
        parameters = {
            "keyword": city_name.upper(),
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(
            url=get_cities, 
            params=parameters, 
            headers=headers_amadeus
        )
        try:
            iata_code = response.json()["data"][0]["iataCode"]
        except IndexError:
            print(f"IndexError: No airport code found for {city_name.upper()}")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name.upper()}")
            return "N/A"
        return iata_code

    def _get_new_token(self):
        headers = {
            "Content-type": "application/x-www-form-urlencoded",
        }

        body = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret,
        }

        response = requests.post(
            url=get_token, 
            headers=headers, 
            data=body
        )
        return response.json()["access_token"]
    
    def check_flight_offers(self, origin_code, destination_code, departure_date, return_date, is_direct=True):
        if is_direct == True:
            is_nonstop = "true"
        elif is_direct == False:
            is_nonstop = "false"
            
        headers = {
            "Authorization": f"Bearer {self._token}"
        }
        # This is your query parameters 
        parameters = {
            "originLocationCode": origin_code,
            "destinationLocationCode": destination_code,
            "departureDate": departure_date.strftime("%Y-%m-%d"),
            "returnDate": return_date.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": is_nonstop,
            "currencyCode": CURRENCY,
            "max": "10",
        }
        response = requests.get(url=get_flights, params=parameters, headers=headers)
        
        # This if for debugging
        if response.status_code != 200:
            print(
                f"response code: {response.status_code}"
                f"response body: {response.text}"
            )
        
        return response.json()
