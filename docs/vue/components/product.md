"Product" - script that defines a component displays a single game product page

Methods:
- addToCart(): method is used to add a product to the shopping cart. It takes in the productId as an argument, adds it to the cart array in the Vuex store, and stores the updated cart array in the local storage. Finally, it navigates to the shopping cart page.
- mounted(): method is a lifecycle hook that runs when the component is mounted. It fetches the game data from the server and stores it in the game property of the component. If the game data is already in the local storage, it retrieves it from there instead of making a network request. It also sets up the slider for the game images by preloading the images and setting the loading property to false when they are loaded.