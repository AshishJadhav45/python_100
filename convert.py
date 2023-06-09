# Convert miles to kilometer using define function 
"""
1.
Question 1
This function converts miles to kilometers (km).

Complete the code to return the result of the conversion.

NOTE: The following items occur outside of the function. Do not try to change the indentations on the associated code or you will receive an error. 

Call the function to convert the trip distance from miles to kilometers. 

Fill in the blank to print the result of the conversion. 

Calculate the round-trip in kilometers by doubling the result, and fill in the blank to print the result. 
"""
def miles_to_km(miles):
    km = miles * 1.60934
    return km

trip_distance_miles = 100

# Convert trip distance from miles to kilometers
trip_distance_km = miles_to_km(trip_distance_miles)

print("Trip distance in kilometers:", trip_distance_km)

# Calculate round-trip in kilometers by doubling the result
round_trip_km = trip_distance_km * 2

print("Round-trip distance in kilometers:", round_trip_km)
