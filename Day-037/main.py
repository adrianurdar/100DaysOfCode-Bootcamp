import requests
import datetime as dt

USERNAME = os.environ.get("USERNAME")
TOKEN = os.environ.get("TOKEN")
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

headers = {
    "X-USER-TOKEN": TOKEN
}

# Format today's date as required by the API
today = dt.datetime.now()
today = today.strftime("%Y%m%d")


def create_account():
    """
    Create an account
    """
    create_account_endpoint = PIXELA_ENDPOINT
    create_account_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    res = requests.post(url=create_account_endpoint, json=create_account_params)
    print(res.text)


def create_graph():
    """
    Create a graph
    """
    create_graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
    create_graph_params = {
        "id": "graph1",
        "name": "Running Graph",
        "unit": "Km",
        "type": "float",
        "color": "sora",
    }

    response = requests.post(url=create_graph_endpoint, json=create_graph_params, headers=headers)
    print(response.text)


def add_pixel():
    """
    Add a new value to the graph
    """
    add_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1"
    add_pixel_params = {
        "date": today,
        "quantity": input("How many KM did you ran today? "),
    }

    res = requests.post(url=add_pixel_endpoint, json=add_pixel_params, headers=headers)
    print(res.text)


def update_pixel():
    """
    Update the quantity already registered as a "Pixel".
    If target "Pixel" not exist, create a new "Pixel" and set quantity.
    """
    update_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1/{today}"
    update_pixel_params = {
        "quantity": input("Enter new value: "),
    }

    res = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=headers)
    print(res.text)


def delete_pixel():
    """
    Delete the registered "Pixel".
    """
    delete_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1/{today}"

    res = requests.delete(url=delete_pixel_endpoint, headers=headers)
    print(res.text)


# Call the action you want to take on your graph
delete_pixel()
