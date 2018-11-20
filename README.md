# techchallenge

## Installation

- Run pip install -r requirements.txt.
- Add 'api' to INSTALLED_APPS.

## Usage

- Run manage.py create_states to create US states.
- Run manage.py ingest_property_csv to handle data in challenge_data.csv file.

## Assumptions

- Most of the fields can be empty.
- A property must have an address.
- State field in the CSV file contains only 'CA'.
- A property might have extra information from different websites.

## PossibleImprovements

- Add more unit tests to test the models, views and commands thoroughly.
- Proper command to pre-populate state data.
