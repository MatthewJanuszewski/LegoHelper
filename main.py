"""
Main function and command line starter.
"""
import csv
from datetime import date

import src.BrickLinkShipping as BrickLinkShipping
import src.BrickOwlShipping as BrickLOwlShipping


def main():
    # Get current date
    today = date.today()
    date_string = today.strftime("%m_%d_%y")

    # Query for packaging weight
    shipping_weight = input("Input shipping material weight in ounces: ")

    # Set up formatting for CSV file
    filename = "shipping_info_" + date_string + ".csv"
    fields = [
        "Full Name",
        "Address 1",
        "Address 2",
        "City",
        "State",
        "Zipcode",
        "Country",
        "Override Weight (Ounces)",
        "Override Length (Inches)",
        "Override Width (Inches)",
        "Override Height (Inches)",
    ]

    # Call functions to query APIs
    brick_link_shipping = BrickLinkShipping.write_shipping_csv(shipping_weight)
    brick_owl_shipping = BrickLOwlShipping.write_shipping_info(shipping_weight)

    # Combine shipping data from both APIs
    shipping_data = brick_link_shipping + brick_owl_shipping

    # Write shipping data to CSV file
    with open(filename, "w") as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        csvwriter.writerow(fields)

        # writing the data rows
        csvwriter.writerows(shipping_data)


if __name__ == "__main__":
    main()
