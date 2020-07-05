# 딕셔너리(Dictionary) : 순서x, 수정o, 삭제o

# 선언
a = {'name': 'kim', 'phone': '010-1234-1234', 'birth': '990604'}
     # 키는 문자열과 숫자로 모두 선언 가능하다.
b = {0: 'hello python', 1: 'hello coding'}
c = {'arr': [1,2,3,4,5]} 
     # 딕셔너리에는 리스트도 value로 지정할수있다.

# 출력
print(a['name']) # 이렇게 직접 접근도 가능하지만
print(a.get('name')) # get함수로 접근하면 해당 키가 없을 경우 
                     # 없다고 표시 해주기 때문에 더 안전하다.
print(c.get('arr')[1:3])

# 딕셔너리 추가
a = {'name': 'kim', 'phone': '010-1234-1234', 'birth': '990604'}

a['address'] = 'Seoul'
print(a)
a['rank'] = [1, 3, 4] # value에 리스트 추가 가능
a['rank2'] = (1, 2, 3) # value에 튜플 추가 가능
print(a)

# keys, values, items(key와 value 한쌍)

a = {'name': 'kim', 'phone': '010-1234-1234', 'birth': '990604'}

print(a.keys()) # key들만 출력

print(a.values()) # value들만 출력

print(a.items()) # item들 출력


# 집합(sets) (순서x, 중복x, 수정o, 삭제o)

# 선언

b = set([1,2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(type(a))
print(c)

t = tuple(b)
print(t)
l = list(b)
print(l)

# 집합 함수

s1= set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1.intersection(s2)) # 교집합
print(s1 & s2) # 이렇게도 가능

print(s1.union(s2)) # 합집합
print(s1 | s2) # 이렇게도 가능

print(s1.difference(s2)) #차집합
print(s1 - s2) # 이렇게도 가능

# 추가 & 제거

s3 = set([7, 8, 10, 15])

s3.add(18)
print(s3)

s3.remove(15)
print(s3)








