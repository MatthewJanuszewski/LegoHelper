"""
Shipping data processor for BrickLink API.
"""
import csv

from bricklink_api.auth import oauth
from bricklink_api.order import get_orders, get_order

import constants


def write_shipping_csv():
    # Set up CSV file formatting
    # PirateShip required field names
    fields = [
        "Name",
        "Address",
        "Address Line 2",
        "City",
        "State",
        "Zipcode",
        "Country",
        "Ounces",
    ]
    # Array for shipping data
    rows = []
    # name of csv file
    filename = "shipping_info.csv"

    # Use BrickBytes API to generate authentication
    consumer_key = constants.consumer_key
    consumer_secret = constants.consumer_secret
    token_value = constants.token_value
    token_secret = constants.token_secret
    auth = oauth(consumer_key, consumer_secret, token_value, token_secret)

    # Call BrickLink API and get list of all orders currently marked as Packed
    api_result = get_orders(status="PACKED", auth=auth)
    orders = api_result.get("data")

    # For each order call the BrickLink API again to retrieve its associated shipping info, then write it to CSV
    for order in orders:
        order_id = order.get("order_id")
        order_shipping_data = get_order(order_id=order_id, auth=auth)
        formatted_shipping_data = [
            order.get("buyer_name"),
            order_shipping_data.get("data")
            .get("shipping")
            .get("address")
            .get("address1"),
            order_shipping_data.get("data")
            .get("shipping")
            .get("address")
            .get("address2"),
            order_shipping_data.get("data").get("shipping").get("address").get("city"),
            order_shipping_data.get("data").get("shipping").get("address").get("state"),
            order_shipping_data.get("data")
            .get("shipping")
            .get("address")
            .get("postal_code"),
            order_shipping_data.get("data")
            .get("shipping")
            .get("address")
            .get("country_code"),
            float(order_shipping_data.get("data").get("total_weight"))
            * 0.035274,  # Convert from oz to g
        ]
        rows.append(formatted_shipping_data)

    # Write shipping data to csv file
    with open(filename, "w") as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        csvwriter.writerow(fields)

        # writing the data rows
        csvwriter.writerows(rows)
