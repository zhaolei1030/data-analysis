import numpy as np
import csv
number = 300
data = np.loadtxt(open("path\position_test({}).csv".format(number),"rb"),delimiter=",",skiprows=0)
# print(data.shape)
out1 = open('position_1({}).csv'.format(number), 'a', newline='')
out2 = open('position_2({}).csv'.format(number), 'a', newline='')
out3 = open('position_3({}).csv'.format(number), 'a', newline='')
out4 = open('position_4({}).csv'.format(number), 'a', newline='')
out5 = open('position_5({}).csv'.format(number), 'a', newline='')
csv1_write = csv.writer(out1, dialect='excel')
csv2_write = csv.writer(out2, dialect='excel')
csv3_write = csv.writer(out3, dialect='excel')
csv4_write = csv.writer(out4, dialect='excel')
csv5_write = csv.writer(out5, dialect='excel')
for i in data:
    if i[number] ==1:
        csv1_write.writerow(i)
    elif i[number] == 2:
        csv2_write.writerow(i)
    elif i[number] == 3:
        csv3_write.writerow(i)
    elif i[number] == 4:
        csv4_write.writerow(i)
    else:
        csv5_write.writerow(i)
