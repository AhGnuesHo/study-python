#연습문제 1번
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

#연습문제 2번
for i in range(1,1001):
    if i%3 == 0:
        print(i)
        
#연습문제 3번
for i in range(1,6):
    for j in range(0,i):
        print("*", end="")
    print("")

#연습문제 4번   
for i in range(1,101):
    print(i)

#연습문제 5번
sum = 0   
for std in [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]:
    sum += std
print(sum/10)

#연습문제 6번
numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n % 2 == 1]
print(result)

#백준 1330
a,b=input().split(" ")
a = int(a)
b = int(b)
if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")

#백준 2753
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("1")
else: print("0")

#백준 14681
x = int(input())
y = int(input())
if x > 0:
    if y > 0: print("1")
    elif y < 0: print("4")
else:
    if y > 0: print("2")
    else: print("3")

#백준 2884
hour,min = input().split(" ")
hour = int(hour)
min = int(min)

if(min >= 45):
    print("%d %d" %(hour, min-45))
else:
    if hour != 0:
        print("%d %d" %(hour-1, min+15))
    else:
        print("%d %d" %(23, min+15))
        
#백준 2525
hour,min = map(int, input().split())
dur = int(input())
if (min+dur) < 60:
    print("%d %d"%(hour, min+dur))
else:
    if (min+dur)//60+hour <= 23:
        print("%d %d"%((min+dur)//60+hour, (min+dur)%60))
    else: print("%d %d"%(hour+(min+dur)//60-24,(min+dur)%60))

#백준 2480
a,b,c = map(int, input().split())
if a == b:
    if b == c:
        print(10000+a*1000)
    else:
        print(1000+a*100)
else:
    if b == c:
        print(1000+b*100)
    elif a == c:
        print(1000+a*100)
    else:
        print(max(a,b,c)*100)

#백준 2739
i = int(input())
for a in range(1,10):
    print("%d * %d = %d" %(i, a, i*a))

#백준 10950
i = int(input())
a = 0
while(a<i):
    j,k= map(int, input().split())
    print(j+k)
    a += 1

#백준 8393
i = int(input())
sum = 0
for a in range(1,i+1):
    sum += a
print(sum)

#백준 15552
import sys

i = int(sys.stdin.readline())
a = 0
while(a<i):
    j,k= map(int, sys.stdin.readline().split())
    print(j+k)
    a += 1

#백준 2741
i = int(input())
for a in range(0,i):
    print(a+1)
 
#백준 2742       
i = int(input())
while(i>0):
    print(i)
    i -= 1

#백준 11021    
i = int(input())
for j in range(0,i):
    a,b=map(int, input().split())
    print("Case #%d: %d"%(j+1, a+b))

#백준 11022
i = int(input())
for j in range(0,i):
    a,b=map(int, input().split())
    print("Case #%d: %d + %d = %d"%(j+1, a, b, a+b))

#백준 2438
i = int(input())
for a in range(1,i+1):
    for j in range(0,a):
        print("*", end="")
    print("")
    
#백준 2439
a = int(input())
for i in range(1,a+1):
    for j in range(a-i, 0, -1):
        print(" ", end="")
    for k in range(0,i):
        print("*", end="")
    print("")
    
#백준 10871
a,b = map(int, input().split())
c = list(map(int, input().split()))
for i in range(0,a):
    if c[i] < b: print(c[i], end=" ")
    
#백준 10952
a,b = map(int, input().split())
while(a!=0 and b!=0):
    print(a+b)
    a,b = map(int, input().split())

#백준 10951
sum = 0
for i in range(500,1000):
    if(i%2==1):
        sum += i
print(sum)

#백준 1110
sum=0
i=0
while(i<=10):
    sum += i
    i += 1
print(sum)