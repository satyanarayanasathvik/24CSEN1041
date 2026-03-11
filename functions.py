def func(x):
    return x*x

print(func(func(2)))
print(func(func(4)))

#Output
"""
16
256
"""

def outer():
    def inner():
        print("Inner function")
    inner()

outer()

#Output
def outer():
    def inner():
        print("Inner function")
    inner()

outer()
inner()

#Output
"""
Inner function
Traceback (most recent call last):
  File "C:/Users/CSE-320-63/Desktop/test.py", line 7, in <module>
    inner()
NameError: name 'inner' is not defined. Did you mean: 'iter'?
"""

#Default Parameters
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Phani")

#Output
"""
Hello Guest
Hello Anu
"""
