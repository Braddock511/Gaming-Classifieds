"Header" - script that defines the behavior of the website header.

Methods:
- hamburgerClick(): toggles the state of the hamburgerFlag data property, which is used to show or hide the mobile navigation menu.
- searchGames(): triggers a search for games based on the searchQuery data property. If searchQuery is empty, it fetches all games from the server and sets the results in the Vuex store. Otherwise, it sets the searchQuery in the Vuex store and navigates to the search results page.
- logout(): clears the user-login-flag cookie and navigates to the home page or refreshes the current page.
- watch: watches for changes in the cart array in the Vuex store and updates the productsCounter data property with the new length of the cart array.