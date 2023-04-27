Python scripts that includes functions to interact with the PostgreSQL database

create_user - insert user login, password, email into database
- login (str): user login
- password (str): user password 
- email (str): user email

check_user - checks if the user exists in database.
- login (str): user login
- password (str): user password 

get_games - retrieve games from database.

create_game - insert new game from user into database
- game (dictionary): infromation about game: 
    - user_id (int): id user that create offer
    - title (str): offer title (max 50 letters)
    - description (str): offer description (max 250 letters)
    - genre (str): game genre
    - platform (str): game platform
    - price (str): offer price
    - image_url (str): game image url

get_credentials - retrieve credentials from database.

add_order - insert payment and delivery into database
- order (dictionary): information about order:
    - email (str)
    - name (str)
    - phone (str)
    - city (str)
    - postal-code (str)
    - address (str)
    - building-number (str)
    - apartment-number (str)
    - instructions (str): additional information to order
    - prducts_id (list): list of id products
    - price (float)