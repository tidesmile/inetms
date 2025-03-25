str='Hello worrd' #ัตัวแปลไว้เรียกใช้งาน
print('This is',str)

def funcl(): #กล่อง Function ไว้เรียกใช้งาน
    print('In funcl')
print('Outside funcl')

def func2():
    return 'In func2'

funcl() #เรียกใช้งาน Function
str2=func2()
print(str2)