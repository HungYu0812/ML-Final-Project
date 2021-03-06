import csv
import json
import pycountry
import numpy as np

# 資料
hotel = {'City Hotel': 1, 'Resort Hotel': 0}
arrival_date_month = {'January': 1, 'February': 2,
                      'March': 3, 'April': 4, 'May': 5, 'June': 6,
                      'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}

meal = {'BB': 1, 'HB': 2, 'SC': 3, 'FB': 4}
market_segment = {'Online TA': 1, 'Corporate': 2,
                  'Offline TA/TO': 3, 'Groups': 4, 'Complementary': 5, 'Aviation': 6, 'Direct': 7}
distribution_channel = {'Direct': 1, 'GDS': 2, 'Corporate': 3, 'TA/TO': 4}
deposit_type = {'Non Refund': 1, 'Refundable': 2, 'No Deposit': 0}
customer_type = {'Transient-Party': np.array([0, 0, 0, 1]),
                 'Transient': np.array([0, 0, 1, 0]), 'Group': np.array([0, 1, 0, 0]), 'Contract':  np.array([1, 0, 0, 0])}
reservation_status = {'Check-Out': 1, 'Canceled': 0}
letter = {}
for i in range(1, 27):
    letter[chr(i+64)] = np.zeros(26)
    letter[chr(i+64)][i-1] = 1

LIST = {'hotel': hotel, 'arrival_date_month': arrival_date_month, 'meal': meal,
        'market_segment': market_segment, 'distribution_channel': distribution_channel, 'reserved_room_type': letter, 'assigned_room_type': letter, 'deposit_type': deposit_type, 'customer_type': customer_type, 'reservation_status': reservation_status}


with open('train.csv', newline='') as csvfile:

    # 讀取 CSV 檔內容，將每一列轉成一個 dictionary
    rows = csv.DictReader(csvfile)
    list = []
    # 以迴圈輸出指定欄位()
    count = 0
    for row in rows:
        for inform in row:
            if inform in LIST:
                try:
                    row[inform] = LIST[inform][row[inform]]
                except:
                    row[inform] = ""
            if inform == 'country':
                try:
                    _country = pycountry.countries.get(alpha_3=row[inform])
                    row[inform] = _country.numeric
                except:
                    pass
                # print(row[inform])
        count = count+1
        list.append(row)
        # if count == 24:
        #   break


def saveJson(list):
    output = json.dumps(list)
    with open('processed_data.json', 'w') as json_file:
        json.dump(output, json_file)


with open('output02.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID', 'hotel', 'is_canceled', 'lead_time',
                  'arrival_date_year', 'arrival_date_month', 'arrival_date_week_number', 'arrival_date_day_of_month', 'stays_in_weekend_nights',
                  'stays_in_week_nights', 'adults', 'children', 'babies', 'meal', 'country', 'market_segment', 'distribution_channel', 'is_repeated_guest',
                  'previous_cancellations', 'previous_bookings_not_canceled', 'reserved_room_type', 'assigned_room_type',
                  'booking_changes', 'deposit_type', 'agent', 'company', 'days_in_waiting_list', 'customer_type', 'adr', 'required_car_parking_spaces', 'total_of_special_requests',
                  'reservation_status', 'reservation_status_date']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for data in list:
        writer.writerow(data)
