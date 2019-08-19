import csv

with open("test.csv",'w') as f:
    writer=csv.writer(f)
    writer.writerow(["wang",'23'])
    writer.writerow(["wangba",'23'])

with open("test.csv",'a') as f:
    writer=csv.writer(f)
    # writer.writerows([[],[],[]])
    writer.writerows([('wang','36'),('ba','45'),('da','45')])