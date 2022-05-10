import math

a=eval(input("a="))
b=eval(input("b="))

c=math.gcd(a,b)
d=a*b/c

print("{},{}的最大公约数：{}；{}，{}的最小公倍数：{}".format(a,b,c,a,b,int(d)))
