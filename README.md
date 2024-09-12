# COFFEE SHOP (OBJECT RELATIONSHIPS)
# OVERVIEW
 - This repository contains a basic implementation of a coffee shop management system using Python.
   The system consists of three primary modules: order.py, customer.py, and coffee.py. 
   Each module defines classes and methods to manage customers, coffees, and orders, and to perform various operations related to them.

## MODULES

1. customer.py
   This module defines the Customer class, which allows for managing customer data and their associated orders. It includes methods for adding orders, retrieving unique coffees ordered, and identifying the customer who has spent the most on a specific coffee.

   Key Features:

 - Initializes customers and tracks all customers.
 - Adds orders and retrieves unique coffees ordered.
 - Identifies the customer who has spent the most on a given coffee.

 2. order.py
    This module defines the Order class along with basic functionalities for creating and managing orders. The Order class tracks all orders placed, including which customer placed the order, which coffee was ordered, and the price.

   Key Features:

 - Initializes orders with coffee, customer, and price.
 - Appends orders to a global list.
 - Includes a method to attempt changing the order price .

 3. coffee.py
    This module defines the Coffee class, which manages coffee details and tracks related orders. It includes methods for retrieving orders, customers who ordered the coffee, and calculating statistics about orders.

   Key Features:

- Initializes coffee with validation.
-  Retrieves all orders and customers associated with the coffee.
-  Calculates the number of orders and average price for the coffee.


## USAGE 
- git clone the repo using https (https://github.com/MavekeJoy/Coffee-code-challenge.git)
- create environment :
    1. python -m venv myenv
    2. source myenv/bin/activate
    
### Running the code 

1. Python3 customer.py
2. Python3 order.py
3. Python3 coffee.py

## DEPENDENCIES
   Python 3.12.3


## LICENSE
   MIT LICENSE

