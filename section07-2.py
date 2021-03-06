# Section07-2
# 파이썬 클래스 상세 이해
# 상속, 다중상속

# 예제 1
# 상속 기본
# 슈퍼 클래스(부모) 및 서브 클래스(자식) -> 모든 속성, 메소드 사용 가능

# 라면 -> 속성(종류, 회사, 맛, 면 종류, 이름) : 부모

class Car: # 부모 클래스를 만들고
    """Parent Class"""
    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def show(self):
        return 'Car Class "Show Method!"'


class BmwCar(Car): # 위에서 부모 클래스를 새로운 클래스 매개변수에 넣으면 상속 받게 된다.
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name
    
    def show_model(self):
        return "Your Car Name : %s" % self.car_name


class BenzCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name
    
    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name
    
    def show(self):
        print(super().show())
        return 'Car Ifo : %s %s %s' % (self.car_name, self.type, self.color)


# 일반 사용
model1 = BmwCar('520d','sedan','red')

print(model1.color) #super
print(model1.type) # super
print(model1.car_name) # sub
print(model1.show()) # Super
print(model1.show_model()) # sub
print(model1.__dict__)

# Method Overriding(오버라이딩)
model2 = BenzCar("220d", "suv", "black")
print(model2.show())


# parent Method call (부모의 메소드를 다이렉트로 콜)
model3 = BenzCar('350s', 'sedan', 'silver')
print(model3.show())

# Inheritance Info(상속 정보)
print(BmwCar.mro())
print(BenzCar.mro())

# 예제2
# 다중 상속

class X():
    pass

class Y():
    pass

class Z():
    pass

class A(X, Y):
    pass

class B(Y, Z):
    pass

class M(B, A, Z):
    pass

print(M.mro())



    




