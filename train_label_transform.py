import csv
import numpy as np
fieldnames = ['arrival_date', 'label']
with open('train_label.csv', newline='') as csvfile:
    bigList = []
    newfield = np.array([])
    for fieldname in fieldnames:
        if fieldname == 'arrival_date':
            newfield = np.append(newfield, 'arrival_date_year')
            newfield = np.append(newfield, 'arrival_date_month')
            newfield = np.append(newfield, 'arrival_date_date')
            continue
        else:
            newfield = np.append(newfield, fieldname)
    bigList.append(newfield)
    rows = csv.DictReader(csvfile)
    for row in rows:
        arr = np.array([[]])
        for fieldname in fieldnames:
            if fieldname == 'arrival_date':
                newElement = row[fieldname].split('-')
            else:
                newElement = row[fieldname]
            arr = np.append(arr, newElement)
        bigList.append(arr)
    np.savetxt('train_label_array.txt', np.array(
        bigList), fmt='%s', delimiter=',')
