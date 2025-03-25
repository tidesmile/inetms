import csv

#csvfile = open('csv1.csv') #เปิดไฟล์ csv
with open('csv1.csv') as csvfile:
    spamreader = csv.reader(csvfile) #อ่านไฟล์ csv ที่ตัวแปล csvfile
    for row in spamreader: # จะเรียก row ใน spamreader จนกว่าข้อมูลจจะครบ
        print(','.join(row)) # ปริ้น ค่า str ของ row ออกมาทั้งหมด
#csvfile.close() #ปิดไฟล์ด้วย ไม่งั้นจะกิน Resource