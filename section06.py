# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def 함수명(parameter):
#   code

# 함수 호출
# 함수명(parameter)

# 함수 선언 위치 중요 (함수 선언은 함수 호출 코드보다 위에 선언 되어야 한다.)

# 예제1
def hello(input):
    print("Hello ", input)

hello("python!")
hello("7777")

# 예제2
def hello_return(input):
    val = "hello " + str(input)
    return val # 변수가 선언된 곳으로 리턴 되어야 저장됨

str1 = hello_return("python!!")
print(str1)

# 예제3(다중 리턴)
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3

val1, val2, val3 = func_mul(100)
print(val1, val2, val3)

# 예제4(데이터 타입 반환)
def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

lt = func_mul2(100)
print(lt)

# 예제5
# *args, **kwargs

def args_func(*args): # 매개변수에 따라 다르게 작동
    print(args)
     
args_func('kim')
args_func('kim', 'park')
args_func('kim', 'park', 'lee')

def args_func(*args):
        for t in args:
            print(t) 
           
args_func('kim')
args_func('kim', 'park')
args_func('kim', 'park', 'lee')

def args_func(*args):
        for i,v in enumerate(args): # 인덱스를 만들어서 순회
           print(i, v)

args_func('kim')
args_func('kim', 'park')
args_func('kim', 'park', 'lee')

 # Kwargs
def kwargs_func(**kwargs):
    print(kwargs)

kwargs_func(name1='kim')
kwargs_func(name1='kim', name2='park', name3='lee')

def kwargs_func(**kwargs):
    for k, v in kwargs.items():
        print(k, y)

kwargs_func(name1='kim')
kwargs_func(name1='kim', name2='park', name3='lee')

# 예제 6
# 전체 혼합
def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

    example_mul(10, 20) # args와 kwargs는 가변 인자이기 때문에 빈 칸으로 나둬도 된다.
    example_mul(10, 20, 'park', kim, ag1=24, age2=35)

# 예제 7
# 중첩함수(클로저)

def nested_func(num):
    def func_in_func(num):
        print(num)
    print("in func")
    func_in_func(num + 10000)

nested_func(10000)

# 예제 8 hint

def func_mul3(x : int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

print(func_mul3(5))

# 람다식 예제
# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(heap 초기화) -> 메모리 초기화


# 일반적 함수 -> 변수 할당
def mul_10(num : int) -> int:
    return num * 10

var_func = mul_10
print(var_func)
print(type(var_func(10)))

# 람다 함수
lambda_mul_10 = lambda num: num * 10

print(lamde_mul_10(10))

def func_final(x, y func):
    print(x * y * func(10))

func_final(10,10,lambda_mul_10)

print(func_final(10, 10, lambda x: x * 1000))






