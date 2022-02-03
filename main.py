"""
Main function and command line starter.
"""
import csv

import src.BrickLinkShipping as BrickLinkShipping
import src.BrickOwlShipping as BrickLOwlShipping


def main():
    filename = "shipping_info.csv"
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
    brick_link_shipping = BrickLinkShipping.write_shipping_csv()
    brick_owl_shipping = BrickLOwlShipping.write_shipping_info()

    shipping_data = brick_link_shipping + brick_owl_shipping

    with open(filename, "w") as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        csvwriter.writerow(fields)

        # writing the data rows
        csvwriter.writerows(shipping_data)


if __name__ == "__main__":
    main()
