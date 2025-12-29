# Final Subtraction Program
# Date Created: 11/2/2023
# Author:Celia Mercier, Danielle Alverson

import csv
import pandas as pd
import matplotlib.pyplot as plt
from classes import Subtract_Save

file_total = ""
file_substrate = ""

result = Subtract_Save.subtract_and_store(file_total, file_substrate)

# Separate coordinates into lists
keys = list(result.keys())
values = list(result.values())

# Parse data from the input files
data1 = Subtract_Save.parse_file(file_total)
data2 = Subtract_Save.parse_file(file_substrate)

keys_data1 = list(data1.keys())
values_data1 = list(data1.values())

keys_data2 = list(data2.keys())
values_data2 = list(data2.values())

plt.figure()

# Plotting data from the first file
plt.plot(keys_data1, values_data1, label='Total Signal', color='blue')

# Plotting data from the second file
plt.plot(keys_data2, values_data2, label='Substrate', color='green')

# Plotting the subtraction values
plt.plot(keys, values, label='Subtraction', color='magenta')
plt.xlabel("q(A^-1)")
plt.ylabel("Intensity")
plt.legend()
plt.show()
