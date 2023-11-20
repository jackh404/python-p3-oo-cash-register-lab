#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
  def add_item(self,title,price,quantity=1):
    self.total += price*quantity
    self.items.append({'title':title,'price':price,'quantity':quantity})
  def apply_discount(self):
    if(self.discount > 0):
      self.total = self.total*(100-self.discount)/100
      print(f"After the discount, the total comes to ${self.total:.0f}.")
    else:
      print("There is no discount to apply.")
  def get_items(self):
    return [item['title'] for item in self.items]
  def void_last_transaction(self):
    if(len(self.items) > 0):
      removed = self.items.pop()
      self.total -= removed['price']*removed['quantity']
    else:
      print("There are no items to remove.")
blah = CashRegister()
blah.add_item("eggs", 1.99, 2)
blah.add_item("tomato", 1.76, 3)
print(blah.get_items())
