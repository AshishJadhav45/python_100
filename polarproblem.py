import cmath

complex_number = complex(input().strip())  # Reading the complex number from input

# Calculating the magnitude (r) and phase angle (θ)
magnitude = abs(complex_number)
phase_angle = cmath.phase(complex_number)

# Printing the polar coordinates
print(magnitude)
print(phase_angle)
