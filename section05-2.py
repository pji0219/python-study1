# 파이썬 흐름제어(반복문)
# 반복문 실습

# 코딩의 핵심 -> 조건 해결 중요

# 기본 반복문 : for, while

v1= 1
while v1 < 11:
    print("v1 is :", v1)
    v1 += 1

for v2 in range(10): # 0부터 9까지 자동으로 할당(0부터 10미만)
    print("v2 is :", v2)

for v3 in range(1,11): # 1부터 10까지 할당(1부터 11미만)
    print("v3 is :", v3)

# 1~ 100 합

sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1

print('1~ 100 : ', sum1)
print('1 ~100 : ', sum(range(1, 101))) # 1부터 100까지 더해라
print('1 ~100 : ', sum(range(1, 101, 2)))# 1부터 100까지 더하는데 짝수
                                         # 단위로

# 시퀀스(순서가 있는)자료형 반복
# 문자열, 리스트, 튜플, 집합, 딕셔너리
# literable 리턴함수 : range, reversed, eumeerate, filter, map, zip

names = ["Kim", "park","cho", "choi", "Yoo"]

for v in names:
    print("You are : ", v)

word = "dreams"

for s in word:
    print("Word : ", s)


my_info = {
    "name" : "kim",
    "age"  : 32,
    "city" : "Seoul"
}

# 기본 값은 키
for key in my_info:
    print("my_info:", key)

# 키
for key in my_info.keys():
    print("my_info:", key)

# 밸류
for value in my_info.values():
     print("my_info:", value)

# 키 and 밸류
for k, v in my_info.items():
     print("my_info:", k, v)

name = "KennRY"

for n in name:
    if n.isupper():
        print(n.lower())
    else:
        print(n.upper())

# break (자기가 찾고자 하는 값이 나오면 즉시 반복문 탈출)
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 33:
        print("found : 33!")
        break
    else:
        print("not found: 33!")

# for - else 구문(반복문이 정상적으로 수행 된 경우 else 블럭 수행)
numbers2 = [14, 3, 4, 7, 10, 24, 17, 2, 37, 15, 34, 36, 38]

for num in numbers2:
    if num == 33:
        print("found : 33!")
        
    else:
        print("not found: 33!")
else:
    print("Not found 33......")

#continue

lt= ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is float:
        continue
    print("타입 : ", type(v))

name = "Niceman"
print(reversed(name))
print(list(reversed(name)))
print(tuple(reversed(name)))







