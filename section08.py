# section 08
# 파이썬 모듈과 패키지

# 패키지 예제
# 상대 경로
# .. : 부모 디렉토리
# .  : 현재 디렉토리

# 사용1(클래스)

from pkg.fibonacci import Fibonacci # pkg 패키지에 fibonacci 모듈의 Fibonacci 클래스 불러옴

F = Fibonacci() # 변수 F에 피보나치 클래스 선언

F.fib(300) # 피보나치 클래스 내에 fib 메소드 사용

print("ex1 : ", F.fib2(400))
print("ex1 : ", F.title)


# 사용2(클래스)
from pkg.fibonacci import * # *은 피보나치 파일 안에 있는 모든 클래스 불러옴

F = Fibonacci() # 변수 F에 피보나치 클래스 선언

F.fib(500) # 피보나치 클래스 내에 fib 메소드 사용

print("ex2 : ", F.fib2(600))
print("ex2 : ", F.title)


# 사용3(함수)
import pkg.calculations as c

print("ex3 : ", c.add(10,100))
print("ex3 : ", c.mul(10,100))

# 사용4(함수)
from pkg. calculations import div as d

print("ex4 : ", int(d(100,10)))

# 사용5
import pkg.prints as p
import builtins
p.prt1()
p.prt2()
print(dir(builtins))




