# Section05-1
# 파이썬 흐름제어(제어문)
# 조건문 실습

print(type(True))
print(type(False))

# 조건문 기본문법
# 예1
if True: # if 뒤에 조건이 들어간다.
    print("Yes")

# 예2
if False:
    print("No") # False이기 때문에 if문 이하는 생략이 된다.

# 예3
if False:
    print("No")
else:
    print("Yes2") # else는 if문이 실행되지 않았을때 실행된다.    

# 관계연산자
# >, >=, <, <=, ==, !=
    
a = 10
b = 0

print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)


# 참 거짓 종류(True, False)
# 참 : "내용" , [내용], (내용), {내용}, 1
      # 내용이 있는 문자열,리스트,튜플,딕셔너리, 숫자1은 참이다.

# 거짓 : "", [], (), {}, 0
        # 빈 문자열, 리스트, 튜플, 딕셔너리, 숫자0은 거짓이다.

a = "1"
b = ""

if a:
    print("True")
else:
    print("false")
     
if b:
    print("True")
else:
    print("False")



# 논리 연산자
# and, or, not

a = 100
b = 60
c = 15

print('and : ', a > b and b > c)
print('or : ', a > b or c > b)
print('not :', not a > b)

# 산술, 관계, 논리 연산자
# 산술 > 관계 > 논리 순서로 적용
print('ex1 : ', 5 + 1 > 0 and not 7 + 3 == 10)

score1 = 90
score2 = 'A'

if score1 >= 90 and score2 == 'A':
    print("합격하셨습니다.")
else:
    print("죄송합니다. 불합격입니다.")

# 다중 조건문
num = 90

if num >= 90:
    print("num 등급 A", num)
elif num >= 80:
    print("num 등급 B", num)
elif num >= 70:
    print("num 등급 C", num)
else:
    print("꽝")

# 중첩 조건문

age = 27
height = 175

if age >= 20:
    if height >= 170:
        print("A지망 지원 가능")
    elif height >= 160:
        print("B지망 지원 가능")
    else:
        print("지원 불가")
else:
    print("20세 이상 지원 가능")
    



     
         
                   

  