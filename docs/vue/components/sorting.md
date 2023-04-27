"TheWelcomeBaner" - script that defines a component used for sorting games. It imports the Axios library for making HTTP requests and exports an object that defines a Vue component.

Methods:
- sortGames(): makes an HTTP GET request to a local server at http://127.0.0.1:8000/get-games with query parameters for the selected genre and platform options, if any. The response data is then stored in the Vuex store under the games state.