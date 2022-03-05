"""
Shipping data processor for BrickOwl API.
"""
import requests
import constants


def write_shipping_info(shipping_weight):
    # Array for shipping data
    rows = []

    # Call BrickOwl API and get a list of all "Processed" orders
    key = constants.brick_owl_key
    payload = {"key": key, "list_type": "store", "status": "Processed"}
    response = requests.get(
        url="https://api.brickowl.com/v1/order/list", params=payload
    )
    response = response.json()
    order_ids = list()
    for order in response:
        order_ids.append(order.get("order_id"))

    # For each order call the BrickOwl API again to retrieve its associated shipping info
    for brick_owl_id in order_ids:
        payload = {"key": key, "order_id": brick_owl_id}
        response = requests.get(
            url="https://api.brickowl.com/v1/order/view", params=payload
        )
        response = response.json()
        formatted_shipping_data = [
            response.get("billing_first_name")
            + " "
            + response.get("billing_last_name"),
            response.get("ship_street_1"),
            response.get("ship_street_2"),
            response.get("ship_city"),
            response.get("ship_region"),
            response.get("ship_post_code"),
            response.get("ship_country"),
            round(
                float(response.get("weight")) * 0.035274 + float(shipping_weight),
                2,
            ),
            10.0,
            6.0,
            1.0,
        ]
        rows.append(formatted_shipping_data)
    return rows
