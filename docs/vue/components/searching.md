"Searching" - script that defines a component for displaying and filtering a list of products/games.

Methods:
- filterClick(): toggles the filterFlag property when the filter button is clicked.
- goToProduct(gameId): sets the id property of the Vuex store to the gameId and navigates to the product detail page.
- watch: contains three watchers that react to changes in the Vuex store's searchQuery and games properties, and the selected property of the component. When a change occurs, the component updates the products array accordingly and clears the searchQuery property.