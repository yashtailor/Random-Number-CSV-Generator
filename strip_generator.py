import csv 
import random as r
import sys

filename = 'tes.csv'

with open(filename, 'w',newline='') as csvfile:
     csvwriter = csv.writer(csvfile)
     for i in range(int(sys.argv[2])):
        main_array = []
        for j in range(int(sys.argv[3])):
            fields = []
            for k in range(int(sys.argv[4])):
                while True:
                    val = int(r.randint(int(sys.argv[5]),int(sys.argv[6])))
                    if val in main_array:
                        continue
                    else:
                        if val == 1:
                            value = "*1"
                            fields.append(value)
                            main_array.append(val)
                        elif val == 2:
                            value = "*2"
                            fields.append(value)
                            main_array.append(val)
                        elif val == 3:
                            value = "*3"
                            fields.append(value)
                            main_array.append(val)
                        elif val == 4:
                            value = "*4"
                            fields.append(value)
                            main_array.append(val)
                        elif val == 5:
                            value = "*5"
                            fields.append(value)
                            main_array.append(val)
                        elif val == 6:
                            value = "*6"
                            fields.append(value)
                            main_array.append(val)
                        elif val == 7:
                            value = "*7"
                            fields.append(value)
                            main_array.append(val)
                        elif val == 8:
                            value = "*8"
                            fields.append(value)
                            main_array.append(val)
                        elif val == 9:
                            value = "*9"
                            fields.append(value)
                            main_array.append(val)
                        else:
                            fields.append(val)
                            main_array.append(val)
                        break
            csvwriter.writerow(fields)
        csvwriter.writerow(["","",""])
     csvfile.close()



