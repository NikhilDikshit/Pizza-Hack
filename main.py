# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 18:35:11 2018

@author: Nikhil Dikshit
"""

from pizzapi import *

# create a customer (first_name, last_name, email, mobile_number, address)
# address(Object): self.street, self.city, self.state, self.zip
customer = Customer('Nikhil', 'Dikshit', 'nikhildksht3@gmail.com', '5516894951', '139 Chestnut Avenue, Jersey City, New Jersey, 07306')
print("\n")
print(customer)

# find nearest dominos store
my_nearest_dominos = StoreLocator.find_closest_store_to_customer(customer)
print("\n")
print(my_nearest_dominos)
print("\n")

# explore the menu
menu = my_nearest_dominos.get_menu()
print(menu.display())
menu.search(Name='Pizza')
# menu.search(Name='Chicken')
# menu.search(Name='Pasta')
print("\n")

# make an order
order = Order.begin_customer_order(customer, my_nearest_dominos)
order.add_item('P12ITHCZ') # add a 12-inch Thin Wisconsin 6 Cheese Pizza
order.add_item('2LCOKE')  # and a 20oz bottle of coke
print(order)

# enter your card details (card_number, expiration_date, cvv, zip)
card = CreditCard('5167895727580865', '0917', '765', '07306')
print(card)
print("\n")

# place your order
order.place()
my_nearest_dominos.place_order(order, card)
