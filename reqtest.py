import requests
r = requests.get('https://inet.co.th')
if r.status_code==200:
    with open('inet.html','w',encoding='utf8') as outfile: #เพิ่ม encoding='utf8' เพื่อให้อ่านได้หลายภาษายิ่งขึ้น
        outfile.write(r.text)

#print (r.text)