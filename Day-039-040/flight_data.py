class FlightData:
    def __init__(self, price, city_from, city_to, airport_from, airport_to, departure_date, return_date, via_city):
        self.price = price
        self.city_from = city_from
        self.city_to = city_to
        self.airport_from = airport_from
        self.airport_to = airport_to
        self.departure_date = departure_date
        self.return_date = return_date
        self.via_city = via_city
