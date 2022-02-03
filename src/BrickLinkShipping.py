"""
Shipping data processor for BrickLink API.
"""
from bricklink_api.auth import oauth
from bricklink_api.order import get_orders, get_order

import constants


def write_shipping_csv():
    # Array for shipping data
    rows = []

    # Use BrickBytes API to generate authentication
    consumer_key = constants.consumer_key
    consumer_secret = constants.consumer_secret
    token_value = constants.token_value
    token_secret = constants.token_secret
    auth = oauth(consumer_key, consumer_secret, token_value, token_secret)

    # Call BrickLink API and get list of all orders currently marked as Packed
    api_result = get_orders(status="PACKED", auth=auth)
    orders = api_result.get("data")

    # For each order call the BrickLink API again to retrieve its associated shipping info
    for order in orders:
        order_id = order.get("order_id")
        order_shipping_data = get_order(order_id=order_id, auth=auth)
        formatted_shipping_data = [
            order_shipping_data.get("data")
            .get("shipping")
            .get("address")
            .get("name")
            .get("full"),
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
            round(
                float(order_shipping_data.get("data").get("total_weight")) * 0.035274
                + 0.75,
                2,
            ),  # Convert from oz to g, add 0.75 oz for packaging
            10.0,
            6.0,
            1.0,
        ]
        rows.append(formatted_shipping_data)
    return rows
