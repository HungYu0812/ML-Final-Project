import numpy as np
# The target of this file is to output the index in train dataset which is corresponding to the date of train_label dataset
print("Load txt file...")
train_data = np.loadtxt('trainFTA.txt', dtype=str, delimiter=',')
train_label_data = np.loadtxt(
    'train_label_array.txt', skiprows=1, dtype=int, delimiter=',')

print("Start analyzing...")
ptdict = {}
record_list = []
for index, fieldname in enumerate(train_data[0]):
    if fieldname == 'is_canceled':
        ptdict[fieldname] = index
    if fieldname == 'arrival_date_year':
        ptdict[fieldname] = index
    if fieldname == 'arrival_date_month':
        ptdict[fieldname] = index
    if fieldname == 'arrival_date_day_of_month':
        ptdict[fieldname] = index
    if fieldname == 'stays_in_weekend_nights':
        ptdict[fieldname] = index
    if fieldname == 'stays_in_week_nights':
        ptdict[fieldname] = index
    if fieldname == 'adr':
        ptdict[fieldname] = index
count = 0
for label_arr in train_label_data:
    count = count+1
    temp_arr = np.array([[]])
    # temp_list = []
    label_year = label_arr[0]
    label_month = label_arr[1]
    label_date = label_arr[2]
    label_rev_level = label_arr[3]
    print('Processing: ' + str(label_year)+'-' +
          str(label_month)+'-' + str(label_date))
    # print(label_rev_level)
    temp_arr = np.append(temp_arr, int(label_year))
    temp_arr = np.append(temp_arr, int(label_month))
    temp_arr = np.append(temp_arr, int(label_date))
    temp_arr = np.append(temp_arr, int(label_rev_level))
    # temp_list.append(temp_arr)
    rev_sum = 0
    # if label_year == 2017:
    #   break
    index_list = []
    for index, train_arr in enumerate(train_data[1:]):
        if int(train_arr[ptdict['arrival_date_year']]) != label_year or int(train_arr[ptdict['arrival_date_month']]) != label_month or int(train_arr[ptdict['arrival_date_day_of_month']]) != label_date:
            continue
        index_list.append(int(index+1))
        rate = 1
        '''
        if int(train_arr[ptdict['is_canceled']]) == 1:
            rate = 0
            # print(label_month, label_date, int(train_arr[ptdict['arrival_date_month']]),
            #     int(train_arr[ptdict['arrival_date_day_of_month']]))
        stay_day = rate * int(train_arr[ptdict['stays_in_weekend_nights']]) + \
            int(train_arr[ptdict['stays_in_week_nights']])
        if stay_day == 0:
            stay_day = 1
        rev_sum = rev_sum+float(train_arr[ptdict['adr']]) * stay_day'''

    temp_arr = np.append(temp_arr, str(index_list))
    # print(temp_arr)
    record_list.append(temp_arr)
# print(record_list)
print(record_list)
# np.savetxt('testDRfile.txt', np.array(record_list), fmt='%f', delimiter=' ')
np.savetxt('labelfile_with_index04.txt', np.array(
    record_list), fmt='%s', delimiter=';')
