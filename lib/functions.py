#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print (f"Hello, {name}!")
    
greet("Naureen")
    
def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
    
greet_with_default()
greet_with_default("Sunny")

def add(num1, num2):
    return (num1+ num2)  
add(45, 55)

def halve(number):
    if not isinstance (number, (float,int)):
        return None
    else:
        return number/2 
x= halve(6)
print(x)
