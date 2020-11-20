# Coffee Machine Documentation
*Documentation created by The App Brewery as part of the \#100DaysOfCode Bootcamp*

## MenuItem Class
### Attributes:
* **name** (str) - The name of the drink. E.g. `“latte”`
* **cost** (float) - The price of the drink. E.g `1.5`
* **ingredients** (dictionary) - The ingredients and amounts required to make the drink. E.g. `{“water”: 100, “coffee”: 16}`

## Menu Class
### Methods:
* **get_items()** - Returns all the names of the available menu items as a concatenated string. E.g. `“latte/espresso/cappuccino”`
* **find_drink(order_name)** - Parameter order_name: (str) - The name of the drinks order. Searches the menu for a particular drink by name. Returns a MenuItem 
object if it exists, otherwise returns `None`.

## CoffeeMaker Class
### Methods:
* **report()** - Prints a report of all resources. 
E.g. 
```
Water: 300ml
Milk: 200ml
Coffee: 100g
```

* **is_resource_sufficient(drink)** - Parameter drink: (MenuItem) The MenuItem object to make. Returns True when the drink order can be made, False if ingredients 
are insufficient. E.g. `True`
* **make_coffee(order)** - Parameter order: (MenuItem) - The MenuItem object to make. Deducts the required ingredients from the resources.

## MoneyMachine Class
### Methods:
* **report()** - Prints the current profit. E.g. `Money: $0`
* **make_payment(cost)** - Parameter cost: (float) - The cost of the drink. Returns True when payment is accepted, or False if insufficient. E.g. `False`
