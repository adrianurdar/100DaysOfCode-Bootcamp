import ezsheets
import os

SHEET_KEY = os.environ["SHEET_KEY"]

sheets = ezsheets.Spreadsheet(SHEET_KEY)
sheet_data = sheets[0]
sheet_data.columnCount = 3
sheet_data.rowCount = 10
rows = sheet_data.getRows()
rows.pop(0)

cities_list = sheet_data.getColumn(1)
cities_list.pop(0)
iata_codes_list = sheet_data.getColumn(2)
iata_codes_list.pop(0)
lowest_price_list = sheet_data.getColumn(3)
lowest_price_list.pop(0)


class DataManager:
    def get_cities(self):
        locations_dict = [
            {'City': city, 'iataCode': iata_code, 'Lowest Price': lowest_price}
            for city, iata_code, lowest_price
            in zip(cities_list, iata_codes_list, lowest_price_list)
        ]

        return locations_dict

    def update_sheet(self, dictionary):
        new_data = [list(column) for column in zip(*[d.values() for d in dictionary])]
        new_data[1].insert(0, "IATA Code")
        sheet_data.updateColumn(2, new_data[1])
