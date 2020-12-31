import csv
from sklearn import preprocessing
import numpy as np
fieldnames = ['ID', 'hotel', 'is_canceled', 'lead_time',
              'arrival_date_year', 'arrival_date_month', 'arrival_date_week_number', 'arrival_date_day_of_month', 'stays_in_weekend_nights',
              'stays_in_week_nights', 'adults', 'children', 'babies', 'meal', 'country', 'market_segment', 'distribution_channel', 'is_repeated_guest',
              'previous_cancellations', 'previous_bookings_not_canceled', 'reserved_room_type', 'assigned_room_type',
              'booking_changes', 'deposit_type', 'agent', 'company', 'days_in_waiting_list', 'customer_type', 'adr', 'required_car_parking_spaces', 'total_of_special_requests',
              'reservation_status', 'reservation_status_date']
dictionary = {'ID': set(), 'hotel': set(), 'is_canceled': set(), 'lead_time': set(), 'arrival_date_year': set(), 'arrival_date_month': set(),
              'arrival_date_week_number': set(), 'arrival_date_day_of_month': set(), 'stays_in_weekend_nights': set(), 'stays_in_week_nights': set(),
              'adults': set(), 'children': set(), 'babies': set(), 'meal': set(), 'country': set(), 'market_segment': set(), 'distribution_channel': set(),
              'is_repeated_guest': set(), 'previous_cancellations': set(), 'previous_bookings_not_canceled': set(), 'reserved_room_type': set(),
              'assigned_room_type': set(), 'booking_changes': set(), 'deposit_type': set(), 'agent': set(), 'company': set(), 'days_in_waiting_list': set(),
              'customer_type': set(), 'adr': set(), 'required_car_parking_spaces': set(), 'total_of_special_requests': set(), 'reservation_status': set(),
              'reservation_status_date': set()}

with open('train.csv', newline='') as csvfile:
    # 讀取 CSV 檔內容，將每一列轉成一個 dictionary
    rows = csv.DictReader(csvfile)
    # 以迴圈輸出指定欄位()
    for row in rows:
        # if row['is_canceled'] == '1' and row['reservation_status'] != 'Canceled':
        #   print(row['is_canceled'], row['reservation_status'])
        # if row['is_canceled'] == '0' and row['reservation_status'] != 'Check-Out':
        #   print(row['is_canceled'], row['reservation_status'])

        for fieldname in fieldnames:
            dictionary[fieldname].add(row[fieldname])
'''
X = np.array(list(dictionary['country']))
# print(X)
Y = X.reshape(-1, 1)
# print(Y)
country = X
Y = np.array(['' 'PAN' 'UGA' 'MEX' 'CMR' 'RWA' 'CYP' 'SYC' 'MWI' 'DNK' 'ITA' 'IDN'
              'CYM' 'BOL' 'AZE'])
# enc = preprocessing.OrdinalEncoder()
enc = preprocessing.OneHotEncoder(categories=[country])
enc.fit(Y.reshape(-1, 1))
enc.transform(['SRB'
Y = np.array(['', 'PAN', 'UGA', 'MEX', 'CMR', 'RWA', 'CYP', 'SYC', 'MWI', 'DNK', 'ITA', 'IDN',
              'CYM', 'BOL', 'AZE'])
X = Y .reshape(-1, 1)
print(X)
country = Y
#enc = preprocessing.OrdinalEncoder()
enc = preprocessing.OneHotEncoder()
#X = [['male', 'from US', 'uses Safari'], ['female', 'from Europe', 'uses Firefox']]
enc.fit(X)
print(enc.transform(X).toarray())'''

# print(dictionary['assigned_room_type'])

'''
for fieldname in fieldnames:
    if fieldname == 'ID':
        continue
    if fieldname == 'reservation_status_date':
        continue
    if fieldname == 'adr':
        continue
    # if fieldname == 'company':
    #    continue
    # if fieldname == 'days_in_waiting_list':
    #    continue
    # if fieldname == 'agent':
    #    continue
    # if fieldname == 'previous_bookings_not_canceled':
    #    continue
    print(fieldname)
    print(dictionary[fieldname])'''
