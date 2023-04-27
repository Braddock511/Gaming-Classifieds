Custom FastApi to connect to Vue

register_user - endpoint for registering a user.
- request with a JSON object in the request body containing the following keys:
    - login (str): user's login name.
    - password (str): user's password.
    - email (str): user's email address.

login - endpoint for logining a user.
- request with a JSON object in the request body containing the following keys:
    - login (str): user's login name.
    - password (str): user's password.

get_games - endpoint for retrieving a list of games.
- genre (str): optional genre of the games to retrieve.
- platform (str): optional platform of the games to retrieve.

get_game - endpoint for retrieving for a game.
- game_id (str): optional id game

order - endpoint for made a order
- request with a JSON object in the request body containing the following keys:
    - order (dictionary): information about order:
        - title (str): offer title (max 50 letters)
        - description (str): offer description (max 250 letters)
        - genre (str): game genre
        - platform (str): game platform
        - price (str): offer price
        - image_url (str): game image url
