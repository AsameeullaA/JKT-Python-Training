import os
import datetime
file = "student.dat"
if os.path.exists(file):
    print('File Exists')
    create = os.path.getctime(file)
    modify = os.path.getmtime(file)
    dt_c = datetime.datetime.fromtimestamp(create)
    dt_m = datetime.datetime.fromtimestamp(modify)
    print('Created Time: ', dt_c)
    print('Modified Time: ', dt_m)
else:
    print('No file with such name')
