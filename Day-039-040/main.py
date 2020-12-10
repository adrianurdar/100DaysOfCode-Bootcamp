from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from users_manager import UserManager

# Create objects
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
new_user = UserManager()


# Create the Customer Acquisition Code. Asks the user for their first name, last name and email. Make sure to
#  get them to type their email twice for validation.
new_user.add_user()


# Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with International Air
#  Transport Association (IATA) codes for each city. Most of the cities in the sheet include multiple airports,
#  you want the city code, not the airport code.
cities = data_manager.get_cities()

for city in cities:
    if city["iataCode"] == "":
        city["iataCode"] = flight_search.get_city_code(city["City"])

data_manager.update_sheet(cities)


# Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the
#  cities in the Google Sheet.
for city in cities:
    try:
        flight_data = flight_search.search_cheapest_flight(city["iataCode"])

        if flight_data.via_city == "":
            msg = f"Only €{flight_data.price} to fly from " \
                  f"{flight_data.city_from}-{flight_data.airport_from} to " \
                  f"{flight_data.city_to}-{flight_data.airport_to}, from " \
                  f"{flight_data.departure_date} to " \
                  f"{flight_data.return_date}.\n\n " \
                  f"https://www.google.com/flights?hl=en#flt={flight_data.airport_from}. " \
                  f"{flight_data.airport_to}.{flight_data.departure_date}*{flight_data.airport_to}. " \
                  f"{flight_data.airport_from}.{flight_data.return_date}"
        else:
            msg = f"Only €{flight_data.price} to fly from " \
                  f"{flight_data.city_from}-{flight_data.airport_from} to " \
                  f"{flight_data.city_to}-{flight_data.airport_to}, from " \
                  f"{flight_data.departure_date} to " \
                  f"{flight_data.return_date}.\n\n" \
                  f"Flight has 1 stopover, via {flight_data.via_city}.\n\n" \
                  f"https://www.google.com/flights?hl=en#flt={flight_data.airport_from}. " \
                  f"{flight_data.airport_to}.{flight_data.departure_date}*{flight_data.airport_to}. " \
                  f"{flight_data.airport_from}.{flight_data.return_date}"

        # If the price is lower than the lowest price listed in the Google Sheet then send a SMS to your own number
        #  with the Twilio API.
        #  The SMS should include the departure airport IATA code, destination airport IATA code, departure city,
        #  destination city, flight price and flight dates.
        if flight_data.price < city["Lowest Price"]:
            notification_manager.send_sms(
                message_to_send=msg
                )
            notification_manager.send_email(
                message_to_send=msg
            )
    except AttributeError:
        continue
