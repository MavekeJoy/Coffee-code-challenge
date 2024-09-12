class Customer:
    all_customers = []
    def __init__(self, name):
        self.name = name
        self.orders = []
        Customer.all_customers.append(self)

    def add_order(self, coffee, price):
        self.orders.append({"coffee": coffee, "price": price})

    def get_coffees(self):
        return list(set(order["coffee"] for order in self.orders))

    @classmethod
    def most_aficionado(cls, coffee):
        max_spender = None
        max_amount = 0
        for customer in cls.all_customers:
            total = sum(order["price"] for order in customer.orders if order["coffee"] == coffee)
            if total > max_amount:
                max_amount = total
                max_spender = customer
        return max_spender


# Create some customers
patience = Customer("Patience")
job = Customer("Job")
joy = Customer("Joy")

# Create some orders
patience.add_order("Latte", 6.0)
patience.add_order("Espresso", 4.5)
job.add_order("Latte", 5.5)
job.add_order("Latte", 5.5)
joy.add_order("Espresso", 4.0)
joy.add_order("Latte", 5.5)

# Test the code
print("Patience's coffees:", patience.get_coffees())
print("Job's coffees:", job.get_coffees())
print("Most aficionado for 'Latte':", Customer.most_aficionado("Latte"))