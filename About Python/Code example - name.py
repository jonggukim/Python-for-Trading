'''
# 네임카드 프로그래밍: basic

# 정보 입력 : 1
name = "kim jong gu"
email = "huhahaza@naver.com"
addr = "seoul"

# 정보 입력 : 2
name1 = "james kim"
email1 = "huhahaza@gmail.com"
addr1 = "pusan"

# 네임카드 정보 출력하기

def print_business_card(name, email, addr):
    print("------------------------------------")
    print("Name:   %s" % name)
    print("E-mail:    %s" % email)
    print("Office Address:    %s" % addr)
    print("------------------------------------")

card1 = BusinessCard()            # 인스턴스의 생성
card1

print(type(card1))

print_business_card(name, email, addr)
print_business_card(name1, email1, addr1)

'''
# Class를 통한 네임카드 프로그래밍

class BusinessCard:             # 클래스의 생성
    def set_info(self, name, email, addr):        # input data의 형식을 지정
        self.name = name
        self.email = email
        self.addr = addr
    def print_info(self):                         # input data 의 출력
        print("------------------------------------")
        print("Name:   ", self.name)
        print("E-mail:    ",  self.email)
        print("Office Address:    ",self.addr)
        print("------------------------------------")



member1 = BusinessCard()                    # instance member1 생성
member1.set_info("dumari Nam", "dumari@ebay.com", "Gangnam-Gu")  # member1의 정보입력
print(member1.print_info())                                      # 입력된 member1의 정보 출력

member2 = BusinessCard()
member2.set_info("dumari Nam2", "dumari2@ebay.com", "Seoul")
print(member2.print_info())

class BusinessCard1:             # 클래스의 생성
    def __init__(self, name, email, addr):        # input data의 형식을 지정
        self.name = name
        self.email = email
        self.addr = addr
    def print_info(self):                         # input data 의 출력
        print("------------------------------------")
        print("Name:   ", self.name)
        print("E-mail:    ",  self.email)
        print("Office Address:    ",self.addr)
        print("------------------------------------")


# Class의 실행과 동시에 인스턴스가 기본적으로 실행 된다: __init__(self):
member3 = BusinessCard1("Test Super", "seeyou@UN.com", "Venis")   # instance member3 생성과 정보 입력
print(member3.print_info())





















