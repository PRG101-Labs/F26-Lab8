#TO-DO: write purpose of this file
# Purpose: invoke module of cashregister class

# import the cashregister class from dog file
from cashregister import CashRegister
def main():
    register = CashRegister()
    register.addItem(2.95)
    register.addItem(3.33)
    print(register.getTotal())
    print(register.getCount())
    register.undo(2.95)
    print(register.getTotal())
    print(register.getCount())
    register.clear()
    print(register.getTotal())
    print(register.getCount())

if __name__ == '__main__':
    main()

