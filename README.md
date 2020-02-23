# Tinder Bot

## Setup

1. `$ pipenv install --dev`

1. download chromedriver, drop into main directory

1. create a src/secrets.py file with variables:

    ```python
    phone='phone_number_all_numbers'
    ```

1. create ./whitelist.txt and ./blacklist.txt with keywords:

    Example:

    ```text
    hiking
    movies
    dogs
    ```

1. `$ pipenv run python src/tinder_bot.py`

## TODO

- [ ] Add debug logging
- [ ] Use regex match instead for white-/star-/blacklist
