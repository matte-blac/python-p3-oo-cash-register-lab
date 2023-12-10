#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
# initialize empty list of items and total
    self.items = []
    self.total = 0
    self.discount = discount

  def add_item(self, title, price, quantity = 1):
    # add item title to list and update total for quantity
    for _ in range(quantity):
      self.items.append(title)
    self.total += price * quantity

  def apply_discount(self):
# check if discount exists, apply if available
    if self.discount == 0:
      print('There is no discount to apply.')
      return
    self.total *= (1 - self.discount / 100)
    print(f'After the discount, the total comes to ${self.total:.0f}.')

  def void_last_transaction(self):
# remove last item and adjust total if items exist
    if not self.items:
        return
    last_item = self.items[-1]
    last_price = last_item[1]
    last_quantity = last_item[2]
    del self.items[-1]
    self.total -= last_price * last_quantity

  def get_total(self):
# return current total amount
    return self.total
  
  def get_items(self):
# return a copy of the item list
    return list(self.items)
  pass
