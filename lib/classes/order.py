
class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

        customer.orders(self)
        customer.coffees(coffee)

        coffee.orders(self)
        coffee.customers(customer)

        @property
        def customer(self):
            return self._customer
        
        @customer.setter
        def customer(self, customer):
            from classes.customer import Customer
            if isinstance(customer, Customer):
                self._customer = customer
            return self._customer
        
        @property
        def order(self):
            return self._order
        
        @order.setter
        def order(self, order):
            from classes.order import Order
            if isinstance(order, Order):
                self._order = order
            else:
                raise Exception




