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

# 예제4
# *args, *kwargs

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










        

    

   











