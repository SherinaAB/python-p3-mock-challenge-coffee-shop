#!/usr/bin/env python3
# import ipdb

from classes.customer import Customer
from classes.order import Order
from classes.coffee import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")

    sherina = Customer("kjkls")
    # print(sherina.name)

    dark = Coffee("dark")
    # dark.name = "not dark"
    # print(dark.name)

    newOrder = Order(sherina, dark, 4)
    print(newOrder.price)

    # print(total_orders)
    # ipdb.set_trace()
