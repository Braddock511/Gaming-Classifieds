"BuyView" - single-file component that contains methods and data for a shopping cart page.

Methods:
- totalPrice(): calculates the total price of the products in the shopping cart by using the reduce method on the cart array.
- buy():  method is called when the customer checks out. It sets the loading property to true, populates the order object with the customer's information and the products in the shopping cart, calculates the total price, and makes a POST request to a server API endpoint to submit the order. If the request is successful, it clears the shopping cart, sets the alert object to display a success message, and redirects the customer to the homepage. If the request fails, it sets the alert object to display a warning message.
- mounted(): hook is called when the component is mounted to the DOM. It loops through the products in the shopping cart, makes a GET request to a server API endpoint to retrieve information about each product, and adds the product information to the cart array. The async/await syntax is used to handle the asynchronous nature of the HTTP requests.
