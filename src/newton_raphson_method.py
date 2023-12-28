import math

def f(x):
    return math.pow(math.e, 2*x) + math.sin(x**2)

def derivative(function, point):
    h = 0.0001
    return (function(point + h) - function(point)) / h

def square_root(number):
    if number == 0: return number

if __name__ == '__main__':

    print("hello, world")
