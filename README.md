# PRG101-Lab8
### Submission Details

In this lab, you will complete three activities. Write the scripts in GitHub codespaces. 
`Please note that you must complete the lab during class hours and show your progress to the professor to receive the marks for the lab.
You have been assigned lab time to work on the lab, we do not appreciate students missing the lab classes.`
For this lab, consider taking screenshots and creating a pdf. For some of the tasks, you will need to capture more than one screenshots to show all the code.


### Lab Objectives

- To be able to use a pre-defined class by creating class objects and calling class methods.
- Understand the instance variables, self parameter, and constructor function.
  
## INVESTIGATION 1: CREATING A SIMPLE CLASS

In Python, a class is a blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class can have. Here's a demonstration of creating a simple class :

A class is defined using the class keyword, followed by the class name and a colon.
```Python
class Dog:
    pass
```

Attributes are variables that belong to the class. These are usually defined in a special method called `__init__`. This method is called automatically when a new object is created from the class. The self parameter is a reference to the current instance/object of the class.
```Python
class Dog:
    def __init__(self, name, breed):
        self._name = name
        self._breed = breed
```

Methods are functions that belong to the class.
```Python
class Dog:
    def __init__(self, name, breed):
        self._name = name
        self._breed = breed

    def bark(self):
        return f"{self._name} says woof!"
```

You can create an object (an instance of a class) by calling the class name with the required arguments.
```Python
my_dog = Dog("Buddy", "Golden Retriever")
```

You can access class methods of an object using dot notation.
```Python
print(my_dog.bark())  # Output: Buddy says woof!
```

## lab8a - class Dog
### Creating class object and calling class method.

- Review the code in the file dog.py. Understand the class definition and how instance variables have been created inside the constructor.
- Open the file dog_tester.py.
- The class dog has been imported.
- Create a new object of the `class Dog` inside `main()` function.
- Call the bark method for the object.
- Run the file using the command: `python ./dog_tester.py`.
- Take a clear screenshot of the `main()` from `dog_tester.py` and the output. Add this screenshot in the pdf.

## lab8b - class Cylinder
### Creating a class method, testing the class independently

- A class `Cylinder` has been created for you in the file `cylinder.py`
- Complete the `volume` method.
- Create a new file called `cylinder_tester.py`
- Add comments in `cylinder_tester.py` to explain the purpose of this file.
- Import `class Cylinder` in the `cylinder_tester.py`.
- Create the `main()` function.
- Create a class object.
- Call both class methods.
- Print the output.
- Run the script from command line using the command: `python ./cylinder_tester.py`.
- Take a clear screenshot of volume() method, `main()` form `cylinder_tester.py` and the output. Add this screenshot in the pdf.


## lab8c - class CashRegister
### Adding instance variable and class method in an existing class to extend the functionality

We did an example of implementing `CashRegister` class. Suppose the CashRegister needs to support a method undo() that undoes the addition of the preceding item. This enables a cashier to quickly undo a mistake. 

- Complete the undo function in `cashregister.py` according to the instructions given.
- Create a new file called `cashregister_tester.py`
- Add comments in `cashregister_tester.py` to explain the purpose of this file.
- Import `class CashRegister` in the `cashregister_tester.py`.
- Add main() function in the `cashregister_tester.py`.
- Test the undo functionality by creating an object of the class and calling the necessary methods inside main() and then calling the main().
- Run the script from command line using the command: `python ./cashregister_tester.py`.
- Take a clear screenshot of undo() method, main() from `cashregister_tester.py` and the output. Add this screenshot in the pdf.


## Lab 8 Sign-Off
- Submit the pdf including the  above mentioned screenshots.
- The screenshot must show your username on github codespaces.
- Make sure screenshots are readable.
- Name your file as: StudentFullName_PRG101_Lab8.pdf
