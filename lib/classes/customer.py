class Customer:
    def __init__(self, name):
        self.name = name

        self._orders = []
        self._coffees = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise ValueError("inside the customer setter")
        
    def orders(self, new_order=None):
        from classes.order import Order
        if isinstance(new_order,Order):
            self._orders.append(new_order)
        return self._orders
    
    def coffees(self, new_coffee=None):
        from classes.coffee import Coffee
        if isinstance(new_coffee,Coffee) and new_coffee not in self._coffees:
            self._coffees.append(new_coffee)
        return self._coffees

    def create_order(self, coffee, price):
        from classes.order import Order
        Order(self,coffee,price)
        
        # From Bart AI:
        # order = Order(coffee, price)
        # self._orders.append(order)
        # return order