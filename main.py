import numpy as np

print("Load txt file...")
train_data = np.loadtxt('trainFTA.txt', skiprows=1, dtype=str, delimiter=',')
train_label_data = np.loadtxt(
    'train_label_array.txt', skiprows=1, dtype=str, delimiter=',')

print("Start analyzing...")


print(train_label_data)
