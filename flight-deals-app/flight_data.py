class FlightData:
    #This class is responsible for structuring the flight data.
    
    def __init__(self, price, origin_code, destination_code, out_date, return_date, stops) -> None:
        self.price = price
        self.origin_airport = origin_code
        self.destination_airport = destination_code
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops
    
def find_cheapest_flight(data):
    # Handle empty data if no flight or Amadeus rate limit exceeded
    if data is None or not data['data']:
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

    # Data from the first flight in the json, make this the first price contender
    first_flight = data['data'][0]
    no_of_stops = len(first_flight["itineraries"][1]["segments"]) - 1
    lowest_price = float(first_flight["price"]["grandTotal"])
    origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = first_flight["itineraries"][0]["segments"][no_of_stops]["arrival"]["iataCode"]
    out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

    # Initialize FlightData with the first flight for comparison
    cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date, no_of_stops)
    # Iterate through all the flight offers and compare prices
    for flight in data["data"]:
        price = float(flight["price"]["grandTotal"])
        if price < lowest_price:
            lowest_price = price  # this updates the lowest price 
            # the rest of the attributes are updated
            origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = flight["itineraries"][0]["segments"][no_of_stops]["arrival"]["iataCode"]
            out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
            cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date, no_of_stops)
            print(f"Lowest price to {destination} is Php{lowest_price}")

    return cheapest_flight
