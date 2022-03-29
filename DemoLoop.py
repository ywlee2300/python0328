#Demoloop.py

print("--파이썬의 판단근거---")
print(bool(0))
print(bool(3))
print(bool(""))
print(bool("데이터"))
print(bool([]))
print(bool([1,2,3]))

lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i > 5:
        break
    print("ITEM:{0}".format(i))

print("--여기까지 실행하면 종료--")

for i in lst:
    if i%2 == 0 :
        continue
    print("ITEM:{0}".format(i))


#수열함수 : range(start, end, step)

item = list(range(10))
print(id(item))
print(item)
item = list(range(1, 11, 2))
print(id(item))
print(item)


lst = list(range(1,11))
result = [i**2 for i in lst if i>5]
print(result)

#반복문에서 필터링하는 함수
lst = list(range(0,40,5))

def getBiggerThan20(i):
    return i>20

iterL = filter(lambda x:x>20, lst)
for item in iterL:
    print("item:{0}".format(item))

a = range(10)
print(a)
print(type(a))