# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: models the cash register in super markets.

# TO DO 1: Complete the functions below according to given instructions. 

class CashRegister:
    def __init__(self):
        self._itemCount = 0
        self._totalPrice = 0.0
        #add an instance variable that you might need to implement undo() method
              
    def addItem(self, price):
        self._itemCount = self._itemCount + 1
        self._totalPrice = self._totalPrice + price
        
    def getTotal(self):
        return self._totalPrice
    
    def getCount(self):
        return self._itemCount
    
    def clear(self):
        self._itemCount = 0
        self._totalPrice = 0.0
        
    #complete the following undo() method
    def undo(self):
        pass
        

