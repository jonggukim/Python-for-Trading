'''
계산기 만들기

## 일반 code
def add(v1, v2)
  return v1+v2
end
def subtract(v1, v2)
  return v1-v2
end

num1 = 10
num2 = 10
p add(num1,num2)
p subtract(num1,num2)

num3 = 30
num4 = 20
p add(num3,num4)
p subtract(num3, num4)


'''

## 객체지향 code

class Cal(object):                  # 계산기 클래스의 정의
    def __init__(self, v1, v2):      # 인입문
        self.v1 = v1                  # 변수의 정의
        self.v2 = v2

    def add(self):                   # 메소드의 정의 - 더하기
        return self.v1 + self.v2

    def subtract(self):             # 메소드의 정의 - 빼기기
        returnself.v1 - self.v2


c1 = Cal(10, 10)
print(c1.add())
print(c1.subtract())
c2 = Cal(30, 20)
print(c2.add())
print(c2.subtract())