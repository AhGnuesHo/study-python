#1
print((80+75+55)/3)
print("\n")

#2
print("홀수?")
print(13%2==1)
print("\n")

#3
a = "881120-1068234"
print("YYYYMMDD: %s"%a[0:6])
print("뒷자리: %s" %a[-7:])

a = "881120-1068234"
b = a.split('-')
yy = int(b[0][0:2])
mm = int(b[0][2:4])
dd = int(b[0][4:6])
other = int(b[1])
print("YY: %d"%yy)
print("MM: %d" %mm)
print("DD: %d" %dd)
print("other: %d" %other)
print("\n")

#4
pin = "881120-1068234"
print(pin[7])

#5
a = "a:b:c:d"
print(a.replace(":","#"))

#6
a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)

#7
a = ['Life', 'is', 'too', 'short']
print((" ").join(a))

#8
a = (1,2,3)
a += (4,)
print(a)

#9
a[[1]] = 'python'
#리스트는 그 값이 변할 수 있기 때문에 Key로 쓸 수 없다.

#10
a = {'A':90, 'B':80, 'C':70}
print(a.pop("B"))

#11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
print(list(set(a)))

#12
#a, b 둘 다 [1,2,3]을 가리키므로 둘 다 [1,4,3]으로 변한다.
