class Customer:
    def __init__(self, name):
        self.name = name

class Order:
    all_orders = []

    def __init__(self, coffee, customer, price):
        if not isinstance(price, (int, float)):
            raise ValueError("Price must be a number")
        self.coffee = coffee
        self.customer = customer
        self.price = price
        Order.all_orders.append(self)

class Coffee:
    all_coffees = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Name must be a string with at least 3 characters")
        self.name = name
        Coffee.all_coffees.append(self)

    def orders(self):
        return [order for order in Order.all_orders if order.coffee == self]

    def customers(self):
        return list(set(order.customer for order in self.orders()))

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        return sum(order.price for order in orders) / len(orders) if orders else 0

# Test code
if __name__ == "__main__":
    espresso = Coffee("Espresso")
    latte = Coffee("Latte")

    patience = Customer("Patience")
    job = Customer("Job")
    charles = Customer("Charles")
    dan = Customer("Dan")

    Order(espresso, patience, 3.50)
    Order(espresso, job, 4.00)
    Order(latte, charles, 5.00)
    Order(latte, dan, 4.50)
    Order(latte, patience, 4.75)

    print(f"Coffee Name: {espresso.name}")
    print(f"Number of Orders for Espresso: {espresso.num_orders()}")
    print(f"Average Price of Espresso: ${espresso.average_price():.2f}")

    print(f"Coffee Name: {latte.name}")
    print(f"Number of Orders for Latte: {latte.num_orders()}")
    print(f"Average Price of Latte: ${latte.average_price():.2f}")

    print(f"Customers for Latte: {[customer.name for customer in latte.customers()]}")