import random
ls1 = []
for i in range(65,90):
    ls1.append(chr(i))
for i in range(97,122):
    ls1.append(chr(i))
            
ls2=[1,2,3,4,5,6,7,8,9,0]

ls3=ls1+ls2

n=0

while n<10:
    n=n+1
    password=[]
    password = password + random.sample(ls3, 8)
    print("第{}个随机生成的密码是：{}".format(n,password))
    print("\n")
