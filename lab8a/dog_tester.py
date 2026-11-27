#TO-DO: write purpose of this file
# Purpose: invoke module of Dog class

# import the Dog class from dog file
from dog import Dog
def main():
    #TO-DO:
    # Create an object of the Dog class, pass appripate attributes values.
    my_dog = Dog("Buddy", "Golden Retriever")
    # Call the .bark() method
    print(my_dog.bark())

if __name__ == "__main__":
  main()
