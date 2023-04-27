"ListingView" - single-file component that contains methods for listing a new game on a platform.

Methods:
- listingGame(): method is an asynchronous function that sends a POST request to the backend API at "http://127.0.0.1:8000/listing-game" with the game details such as title, description, genre, platform, price, and image. The response from the API is stored in the response variable, and depending on the status of the response, the method sets the alert variable to either a success message or a warning message, and may redirect the user to the home page using $router.push("/").