# salary = int(input("Enter salary amout:"))

# if not 2000 < salary < 5000:
#     raise ValueError("Not a valid salary!")

# # Defining Custom Exception 

# # this is example of defingin custom Exception

#     class CustomError(Exception):
#         pass
# try:
# # except CustomError:
try: 
    num = int(input("Enter a number!"))
except ValueError:
    print("Number enter is not a interger!")

