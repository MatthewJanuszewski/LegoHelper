# LegoHelper

Simple program for writing shipping information from BrickLink and BrickOwl orders to a CSV file for PirateShip.

### Installation
Make sure to install all required Python packages if working with this source code by running:

`pip install -r requirements.txt`

### API Tokens
To include BrickLink API tokens create a file named `constants.py` at the top level of this repo (under \LegoHelper\) 
and include the following constants in the file: 

`consumer_key = "YOUR_CONSUMER_KEY"`

`consumer_secret = "YOUR_CONSUMER_SECRET"`

`token_value = "YOUR_TOKEN_VALUE"`

`token_secret = "YOUR_TOKEN_SECRET"`

Find your token values by following the directions at `https://www.bricklink.com/v3/api.page`

For your BrickOwl Key go to `https://www.brickowl.com/api_docs` to find your key and add the following constant to `constants.py`

`brick_owl_key = "YOUR_BRICK_OWL_KEY`

These values need to set up for each individual BrickLink/BrickOwl account and allow full access to your account, so do not share them 
or check them into any public repository.

### Credits
This tool was written by Matthew Januszewski using the excellent BrickBytes Python library by Michael Bugert and Szieberth Ádám 
`https://github.com/BrickBytes/bricklink_api`