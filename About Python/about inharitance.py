# 상속이란 본래의 개체를 기반으로 기능을 추가한 것.
class Class1(object):
    def method1(self): return 'm1'


c1 = Class1()
print(c1, c1.method1())


class Class3(Class1):                    # Class3가 Class1을 상속한다  >>> Class1의 기능을 갖는다.
    def method2(self): return 'm2'

'''
## ruby
class Class 3 < Class 1                      # Class3가 Class1을 상속한다  >>> Class1의 기능을 갖는다.

'''
c3 = Class3()
print(c3, c3.method1())
print(c3, c3.method2())


class Class2(object):                    # 상속 없이 실행 하는경우.
    def method1(self): return 'm1'
    def method2(self): return 'm2'


c2 = Class2()
print(c2, c2.method1())
print(c2, c2.method2())


#   ==============================
# 상속을 통한 계산기 기능 추가
class Cal(object):
    def __init__(self, v1, v2):
        if isinstance(v1, int):
            self.v1 = v1
        if isinstance(v2, int):
            self.v2 = v2
    def add(self):
        return self.v1+self.v2
    def subtract(self):
        return self.v1-self.v2
    def setV1(self, v):
        if isinstance(v, int):
            self.v1 = v
    def getV1(self):
        return self.v1
class CalMultiply(Cal):                 # 곱하기 기능 추가
    def multiply(self):
        return self.v1*self.v2
class CalDivide(CalMultiply):           # 나누기 기능 추가
    def divide(self):
        return self.v1/self.v2
c1 = CalMultiply(10,10)
print(c1.add())
print(c1.multiply())
c2 = CalDivide(20,10)
print(c2, c2.add())
print(c2, c2.multiply())
print(c2, c2.divide())


'''
## ruby
class Cal
  attr_reader :v1, :v2
  attr_writer :v1
  def initialize(v1,v2)
    @v1 = v1
    @v2 = v2
  end
  def add()
    return @v1+@v2
  end
  def subtract()
    return @v1-@v2
  end
  def setV1(v)
    if v.is_a?(Integer)
      @v1 = v
    end
  end
  def getV1()
    return @v1
  end
end
class CalMultiply < Cal
  def multiply()
    return @v1*@v2
  end
end
class CalDivide < CalMultiply
  def divide()
    return @v1/@v2
  end
end
c1 = CalMultiply.new(10,10)
p c1.add()
p c1.multiply()
c2 = CalDivide.new(20, 10)
p c2, c2.add()
p c2, c2.multiply()
p c2, c2.divide()

'''
# 다중 상속 (multiple inheritance )
# >>> 다중 상속은 하나의 클래스가 여러 클래스의 기능을 상속 받는 것.

class C1():
    def c1_m(self):
        print("c1_m")

    def m(self):
        print("C1 m")


class C2():
    def c2_m(self):
        print("c2_m")

    def m(self):
        print("C2 m")


class C3(C2, C1):
    def m(self):
        print("C3 m")


c = C3()
c.c1_m()
c.c2_m()
c.m()
print(C3.__mro__)   # 다중 상속시 우선 순위 (<class '__main__.C3'>, <class '__main__.C2'>, <class '__main__.C1'>, <class 'object'>)






























