import json
import csv
file = open('MMM.txt','r')
with open("mmm.csv","wb") as f:
    writer = csv.writer(f)
    for line in file.readlines():
        json_obj = json.loads(line)
        writer.writerow([json_obj["Low"],json_obj["High"],json_obj["Close"],json_obj["Date"]])
f.close()
file.close()
