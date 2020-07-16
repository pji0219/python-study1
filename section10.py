#Section 10
# 파이썬 예외처리의 이해

# 예외(에러) 종류
# 문법적으로 에러가 없지만, 코드 실행(런타임)프로세스에서 발생하는 예외 처리도 중요
# linter : 코드 스타일, 문법 체크

# SyntaxError : 잘못된 문법

# print('Test) 예외
# if True 예외
#    pass
# x => y 예외

# NameError : 참조변수 없음

a = 10
b = 15

# print(c) 예외

# ZeroDvisionError : 0 나누기 에러
# print(10 / 0) 예외

# IndexError : 인덱스 범위 오버

x = [10, 20, 30]
print(x[0])
# print(x[3]) # 예외 발생

# keyError

dic = {'name': 'kim', 'age': 33, 'city': 'seoul'}

# print(dic['hobby']) 예외
print(dic.get('hobby')) # get으로 접근하면 없는 키는 없다고 나와서 안전

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외

import time
print(time.time())
# print(time.month()) 예외

# ValueError : 참조 값이 없을 때 발생
x = [1, 5, 9]

# x.remove(10) 예외
# x.index(10) 예외


# FileNotFoundError

# f = open('test.txt', 'r') 예외


# TypeError

x = [1,2]
y = (1,2)
z = 'test'

# print(x + y) 예외
# print(x + z) 예외

print(x + list(y)) # 똑같은 자료형으로 형변환을 해서 더해야 예외가 안난다.

# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생시 예외 처리 코딩 권장(EAFP 코딩 스타일)


# 예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명1 여기선 에러를 잡는다.
# except : 에러명2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행

# 예제1

name = ['Kim', 'Lee', 'Park']

try:
    z = 'Kim' #  없는거 쓸 경우 예외 발생
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError:
    print('Not found it! - Occurred ValueError!')
else:
    print('ok! else!')


# 예제2
try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except: # 어떤 에러가 날지 모를 경우에는 에러명 안적어도 됨
    print('Not found it! - Occurred Error!')
else:
    print('ok! else!')


# 예제3
try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError:
    print('Not found it! - Occurred ValueError!')
else:
    print('ok! else!')
finally:
    print('finally ok!')


# 예제4
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴

try:
    print('Try')
finally:
    print('ok Finally!!')


# 예제5
try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError:
    print('Not found it! - Occurred ValueError!')
except IndexError:
    print('Not found it! - Occurred IndexError!')
except Exception: # Exception을 적으나 안적으나 같지만 명시적으로 적는것이 좋다.
    print('Not found it! - Occurred Error!')
else:
    print('ok! else!')
finally:
    print('finally ok!')


# 예제6
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = 'Kim'
    if a== 'Kim':
        print('Ok 허가!')
    else:
        raise ValueError
except ValueError:
    print('문제 발생!')
except Exception as f:
    print(f)
else:
    print('ok!')


