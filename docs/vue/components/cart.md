"Cart" - script that defines shopping cart

Methods:
- totalPrice() calculates and returns the total price of all products in the cart.
- deleteGame(game) deletes the specified game object from the cart array, as well as its corresponding product ID from the Vuex store. If the cart is empty after the deletion, the component redirects the user to the homepage.
- goToProduct(gameId) sets the game ID to the specified value in the Vuex store and redirects the user to the product page for that game.
- mounted() is a lifecycle hook that is called when the component is mounted on the page. It initializes the cart by retrieving each game object from the server using its ID stored in the Vuex store. It updates the cart array with the retrieved game objects.
- watch listens to changes in the cart array in the Vuex store and updates the productsCounter property accordingly.