import numpy as np

print("Load txt file...")
train_data = np.loadtxt('trainFTA.txt', dtype=str, delimiter=',')
train_label_data = np.loadtxt(
    'labelfile_with_index04.txt', dtype=str, delimiter=';')
print("Start analyzing...")
train_label_arr = train_label_data[:, :4]
train_label_index_arr = train_label_data[:, 4]
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

for label_arr in train_label_arr:
    temp_arr = np.array([[]])
    label_year = int(float(label_arr[0]))
    label_month = int(float(label_arr[1]))
    label_date = int(float(label_arr[2]))
    label_rev_level = int(float(label_arr[3]))
    #label_train_index = label_arr[4]
    print('Processing: ' + str(label_year)+'-' +
          str(label_month)+'-' + str(label_date))
    temp_arr = np.append(temp_arr, label_rev_level)
    rev_sum = 0
    for train_arr in train_data[1:]:
        if int(train_arr[ptdict['arrival_date_year']]) != label_year or int(train_arr[ptdict['arrival_date_month']]) != label_month or int(train_arr[ptdict['arrival_date_day_of_month']]) != label_date:
            continue
        rate = 1
        if int(train_arr[ptdict['is_canceled']]) == 1:
            rate = 0
        stay_day = int(train_arr[ptdict['stays_in_weekend_nights']]) + \
            int(train_arr[ptdict['stays_in_week_nights']])
        if stay_day == 0:
            stay_day = 1
        rev_sum = rev_sum+rate*float(train_arr[ptdict['adr']]) * stay_day
    temp_arr = np.append(temp_arr, rev_sum)
    record_list.append(temp_arr)

np.savetxt('testDRfile.txt', np.array(
    record_list), fmt='%f', delimiter=' ')
