# for creating folder 
import os
for i in range(0,100):
    os.mkdir(f"College/day {i+1}")


# for delete the folder

import os 

for i in range(0,100):
    os.rmdir(f"College/days {i+1}")

# for rename the folder

import os

for i in range(0,100):
    os.rename(f"College/days {i+1}",f"College/Day {i+1}")
