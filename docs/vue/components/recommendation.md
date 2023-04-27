"Recommendation" - script that defines a component page for displaying a list of games and navigating to their individual product pages.

Methods:
- goToGenre(genre): This method takes a genre as an argument and makes a GET request to the server to retrieve all games with that genre. It then updates the games array in the data object with the retrieved games and navigates to the search view page.
- goToProduct(gameId): This method takes a gameId as an argument and sets the id property of the games store to the gameId, removes any previously saved game data from local storage, and navigates to the individual product page.