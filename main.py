"""
Main function and command line starter.
"""
import src.BrickLinkShipping as BrickLinkShipping


def main():
    BrickLinkShipping.write_shipping_csv()
    return 0


if __name__ == "__main__":
    main()
