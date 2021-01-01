import csv
from sklearn import preprocessing
import numpy as np
from checkItemInColumn import*

dataSize = 91530

# onehotList = ['hotel', 'meal', 'country', 'market_segment', 'distribution_channel', 'reserved_room_type', 'assigned_room_type','deposit_type', 'agent', 'company', 'customer_type', 'reservation_status']
hotel_enc = preprocessing.OneHotEncoder()
meal_enc = preprocessing.OneHotEncoder()
country_enc = preprocessing.OneHotEncoder()
market_segment_enc = preprocessing.OneHotEncoder()
distribution_channel_enc = preprocessing.OneHotEncoder()
reserved_room_type_enc = preprocessing.OneHotEncoder()
assigned_room_type_enc = preprocessing.OneHotEncoder()
deposit_type_enc = preprocessing.OneHotEncoder()
agent_enc = preprocessing.OneHotEncoder()
company_enc = preprocessing.OneHotEncoder()
customer_type_enc = preprocessing.OneHotEncoder()
reservation_status_enc = preprocessing.OneHotEncoder()
onehotDict = {'hotel': hotel_enc, 'meal': meal_enc, 'country': country_enc, 'market_segment': market_segment_enc,
              'distribution_channel': distribution_channel_enc,
              'reserved_room_type': reserved_room_type_enc, 'assigned_room_type': assigned_room_type_enc, 'deposit_type': deposit_type_enc,
              'agent': agent_enc, 'company': company_enc, 'customer_type': customer_type_enc, 'reservation_status': reservation_status_enc}
for key in onehotDict:
    tempArr = np.array(list(dictionary[key]))
    onehotArr = tempArr.reshape(-1, 1)
    onehotDict[key].fit(onehotArr)
# print(onehotDict['meal'].categories_[0])
arrival_date_month = {'January': 1, 'February': 2,
                      'March': 3, 'April': 4, 'May': 5, 'June': 6,
                      'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
with open('train.csv', newline='') as csvfile:
    bigList = []
    newfield = np.array([])
    for fieldname in fieldnames:
        if fieldname == 'ID':
            continue
        if fieldname not in onehotDict:
            newfield = np.append(newfield, fieldname)
        else:
            newfield = np.append(
                newfield, onehotDict[fieldname].categories_[0])
    bigList.append(newfield)
    # f.write(','.join(newfield))
    # f.write('\n')
    rows = csv.DictReader(csvfile)
    count = 0
    for row in rows:
        if count % 100 == 0:
            print("Processing: " + str(count) + "//"+str(dataSize))
        arr = np.array([[]])
        for fieldname in fieldnames:
            newElement = row[fieldname]
            if fieldname == 'ID':
                continue
            if fieldname == 'arrival_date_month':
                newElement = arrival_date_month[row[fieldname]]
            if fieldname in onehotDict:
                newElement = onehotDict[fieldname].transform(
                    np.array(row[fieldname]).reshape(-1, 1)).toarray()
            arr = np.append(arr, newElement)
        count = count+1
        bigList.append(arr)
        # f.write(','.join(arr))
        # f.write('\n')
        # if count > 3:
        #    break
    # print(len(bigList[2]))
    np.savetxt('trainFTA.txt', np.array(bigList), fmt='%s')
