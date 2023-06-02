with open('file.txt', 'r') as f:
  # Read the first 10 bytes
  data = f.read(10)
  # Save the current position
  current_position = f.tell()
  # Seek to the saved position
  f.seek(current_position)