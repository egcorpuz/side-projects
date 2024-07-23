from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta
import flight_data
import time

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

ORIGIN_CODE = "MNL"

start_date = datetime.now() + timedelta(days=2)  # start in two days
end_date = datetime.now() + timedelta(days=(30*6))  # date in 6 months

# Checks to see if IATA codes are provided
    
for row in sheet_data:
    if row["iataCode"] == "":
        flight_search = FlightSearch()
        row["iataCode"] = flight_search.get_destination_code(row["city"])

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

# Start checking for flights for each city in the spreadsheet
for cities in sheet_data:
    flight_search = FlightSearch()
    flights = flight_search.check_flight_offers(
        origin_code=ORIGIN_CODE, 
        destination_code=cities["iataCode"], 
        departure_date=start_date, 
        return_date=end_date
    )
    if flights is None or not flights["data"]:
        flights = flight_search.check_flight_offers(
            origin_code=ORIGIN_CODE, 
            destination_code=cities["iataCode"], 
            departure_date=start_date, 
            return_date=end_date,
            is_direct=False
        )
    cheapest_flight = flight_data.find_cheapest_flight(flights)
    
    if float(cheapest_flight.price) < float(cities["lowestPrice"]):
        print("This happened. Probably. Check for bugs.")
        whatsapp_alert = NotificationManager(cheapest_flight)
        whatsapp_alert.send_alert()
        
    # Prints cheapest flight for each destination city
    print(f"Your starting price is: PHP{cities['lowestPrice']}")
    print(f"{cities['city']}: PHP{cheapest_flight.price}")
    time.sleep(2)
