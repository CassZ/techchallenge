# techchallenge

## Installation

- Run  pip install -r requirements.txt.
- Add 'api' to INSTALLED_APPS.

## Usage

- Run manage.py create_states to create US states.
- Run manage.py ingest_property_csv to handle data in challenge_data.csv file.

## Assumptions
- Most of the fields can be empty.
- A property might have extra information from different websites.

## PossibleImprovements
- Add unit tests.
- Proper command to pre-populate state data.
