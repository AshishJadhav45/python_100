def count_upper_lower_chars(string):
    upper_count = 0
    lower_count = 0

    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count



input_string = "Hello World"
upper, lower = count_upper_lower_chars(input_string)

print("Total Uppercase characters:", upper)
print("Total Lowercase characters:", lower)
