salary = int(input("Enter salary amout:"))

if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary!")

# # Defining Custom Exception 

#     class CustomError(Exception):
#         pass
# try:
# except CustomError:
