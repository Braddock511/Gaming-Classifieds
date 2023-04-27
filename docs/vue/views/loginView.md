"LoginView" - single-file component that defines a login form for a user. The form contains two input fields for the user's login, password, and a "Login" button. When the user submits the form, the server sends a POST request to a local endpoint /login to login the user. If the registration is login, the user is redirected to the home page after a two-second delay. Otherwise, an alert is displayed on the screen.

Methods:
- loginUser():  This method is called when the user clicks the "Login" button in the form. It sends a POST request to endpoint /login with the user's login and password as data.
