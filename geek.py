# seek() function

with open('file.txt', 'r') as f:
  # Move to the 10th byte in the file
  f.seek(10)
  # Read the next 5 bytes
  data = f.read(5)