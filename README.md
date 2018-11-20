# Technical Challenge

## Installation

- Run pip install -r requirements.txt.
- Add 'api' to INSTALLED_APPS.

## Usage

- Run manage.py create_states to create US states.
- Run manage.py ingest_property_csv to handle data in challenge_data.csv file.
- View Property objects at /properties/
- View ZillowInformation objects at /zillowinformation/
- View Address objects at /addresses/
- View State objects at /states/
- View Documentation at /docs/


## Assumptions

- Most of the fields can be empty.
- A property must have an address.
- State field in the CSV file contains only 'CA'.
- A property might have extra information from different websites.

## Possible Improvements

- Add more unit tests to test the models, views and commands thoroughly.
- Proper command to pre-populate state data.
