class Coffee:

    def __init__(self, name):
        self.name = name
        self._orders = []
        self._customers = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if isinstance(name, str) and not hasattr(self,'name'):
            # Stephen's process???  
            self._name = name
        else:
            raise ValueError("inside the coffee setter")
        
    def orders(self, new_order=None):
        from classes.order import Order
        if isinstance(new_order,Order):
            self._orders.append(new_order)
        return self._orders
    
    def customers(self, new_customer=None):
        from classes.customer import Customer
        if isinstance(new_customer,Customer) and new_customer not in self._customers:
            self._customers.append(new_customer)
        return self._customers

    
    def num_orders(self):
        return len(self._orders)
    
    def average_price(self):
        return sum([order.price for order in self._orders]) / len(self._orders)
        # total_orders = ((sum(self._price)) * (count(self.orders)))/ len(self._orders)

        # return total_orders
        # print(total_orders)




