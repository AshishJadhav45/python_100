def factorial(num):
    if (num == 1 or num ==0):
        return 1
    else:
        return(num*factorial(num-1))
num = 7 
print("Number:",num)
print("factorial:",factorial(num))

'''
Factorial of a positive integer (number) is the sum of multiplication of all the integers smaller than that positive integer. For example, factorial of 5 is 5 * 4 * 3 * 2 * 1 which equals to 120.
'''