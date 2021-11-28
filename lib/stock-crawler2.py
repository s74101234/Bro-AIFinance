import requests
import json
import csv
import time



def crawler(start_time,end_time,stock_num): #start_time,end_time => yyyymmdd ,ex:20170101. 
    for stime in range(start_time,end_time,100):
        # time.sleep(40) #stop the program at a specific time
        web_1="https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date="+ str(stime) +"&stockNo=" + str(stock_num)
        res=requests.get(web_1)
        json_1=json.loads(res.text) 
        output_file=open(r"D:/下載/股票/"+str(stock_num)+".csv",'a',newline="")
        output_writer=csv.writer(output_file)
        # output_writer.writerow(json_1['fields']) #Add title
        for data in(json_1['data']):
            output_writer.writerow(data)
        output_file.close()
    

crawler(20170101, 20171231, 2030)
#start_time and end_time must be same year