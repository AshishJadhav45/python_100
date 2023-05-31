try:
    num = int(input("Enter a interger:"))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("integer Accepted.")
finally:
    print("this is always executed.")

