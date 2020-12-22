import csv
import json
import pycountry

# 資料

hotel = {'City Hotel': 1, 'Resort Hotel': 0}
arrival_date_month = {'January': 1, 'February': 2,
                      'March': 3, 'April': 4, 'May': 5, 'June': 6,
                      'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}

meal = {'BB': 1, 'HB': 2, 'SC': 3, 'FB': 4}
market_segment = {'Online TA': 1, 'Corporate': 2,
                  'Offline TA/TO': 3, 'Groups': 4, 'Complementary': 5, 'Aviation': 6, 'Direct': 7}
distribution_channel = {'Direct': 1, 'GDS': 2, 'Corporate': 3, 'TA/TO': 4}
deposit_type = {'Non Refund': 1, 'Refundable': 2, 'No Deposit': 3}
customer_type = {'Transient-Party': 1,
                 'Transient': 2, 'Group': 3, 'Contract': 4}
reservation_status = {'Check-Out': 1}
LIST = {'hotel': hotel, 'arrival_date_month': arrival_date_month, 'meal': meal,
        'market_segment': market_segment, 'distribution_channel': distribution_channel, 'deposit_type': deposit_type, 'customer_type': customer_type, 'reservation_status': reservation_status}


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
                    pass
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
output = json.dumps(list)
with open('processed_data.json', 'w') as json_file:
    json.dump(output, json_file)
