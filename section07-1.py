# Section07-1
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요
# 네임스페이스 : 객체를 인스턴스화 할 떄 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체 보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용

# 선언
# class 클래스명:
#    함수
#    함수


# 예제1  클래스명은 첫글자가 대문자로 하는것을 원칙 단어와 단어가 연결될때도 다음 단어 첫글자는 대문자 원칙
#클래스는 두가지 형태로 구성 되는데 보통 속성, 메소드로 구성
class UserInfo:
    def __init__(self): # 이것은 클래스를 최초 초기화할떄 호출되는 함수이고 기본적으로 클래스 안에서 구현 해줘야 한다.
        print("초기화")

user1 = UserInfo() # 클래스가 user1 변수에 할당되는 순간 클래스 안에 있는 init 함수가 호출이 되고 함수 안에 적어준 print문이 실행 되어 초기화가 출력이 된다



# 클래스를 하나 생성해서
class UserInfo1:
    def __init__(self, name):
        self.name = name
    def user_info_b(self):
        print("Name: ", self.name)


# user1과 user2라는 변수를 인스턴스화 시켜서 사용하는데 이 인스턴스화 된 변수들은 네임스페이스라는 독립적인 창고를 이용해서 그 안에 name을 저장하고 있다.
# 네임스페이스
user1 = UserInfo1("Kim")# user1변수에 UserInfo1("Kim") 할당
print(user1.name)
# user1.uer_info_b() # user_info_b(self)메소드 호출 *오류가 나서 임시로 주석 처리*
user2 = UserInfo1("park")
print(user2.name)
user2.user_info_b()

print(id(user1))# 네임스페이스 증명하기 위한 메모리 주소값 출력
print(id(user2))

print(user1.__dict__) # 네임스페이스 출력
print(user2.__dict__)


