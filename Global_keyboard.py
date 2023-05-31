x = 13


def my_function():
    global x
    x = 5 # this will change the value of global variable x 
    y = 5 #local variable

my_function()
print(x)
# print(y)