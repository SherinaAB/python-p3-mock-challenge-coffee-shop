
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

        coffee.orders(self)
        coffee.customers(customer)

        customer.orders(self)
        customer.coffees(coffee)
        # where do the above get justified within the components????

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,price):
        if isinstance(price, (int,float)) and 1 <= price <= 10:
            self._price = price
        else:
            raise ValueError("inside the order setter")
        
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self,customer):
        from classes.customer import Customer
        if isinstance(customer,Customer):
            self._customer = customer
        else:
            raise ValueError ("inside the customer order setter")
        
        return self._customer
        
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self,coffee):
        from classes.coffee import Coffee
        if isinstance(coffee,Coffee):
            self._coffee = coffee
        else:
            raise ValueError ("inside the coffee order setter")
        
        return self._coffee