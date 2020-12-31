import numpy as np

letter = {}
for i in range(1, 27):
    letter[chr(i+64)] = np.zeros(26)
    letter[chr(i+64)][i-1] = 1

print(letter)
