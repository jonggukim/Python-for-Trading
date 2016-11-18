# on the ruby
'''
require 'date'
d1 = Date.new(2000, 1, 1)
d2 = Date.new(2010, 1, 1)
p d1.year()                    # instance 맴버
p d2.year()                    # instance 맴버
p Date.today()                 # Class 맴버

=========================

class Cs
  def Cs.class_method()        # 해당 method가 class에 속해있다는 정의 : Cs.~
    p "Class method"
  end
  def instance_method()
    p "Instance method"
  end
end
i = Cs.new()
Cs.class_method()
i.instance_method()
#Cs.instance_method() 오류발생
#i.class_method() 오류발생

'''


class Cs:
    @staticmethod
    def static_method():
        print("Static method")
    @classmethod
    def class_method(cls):
        print("Class method")
    def instance_method(self):
        print("Instance method")
i = Cs()
Cs.static_method()
Cs.class_method()
i.instance_method()


## 클래스 변수
'''
# ruby code : 클래스 변수
class Cs
  @@count = 0                 # <<<< 클래스의 변수 설정
  def initialize()            # 초기화(인스턴스가 시작될때마다) 할때 마다 1씩 증가
    @@count = @@count + 1
  end
  def Cs.getCount()           # class "Cs"의 methoed로 설정
    return @@count
  end
end
i1 = Cs.new()
i2 = Cs.new()
i3 = Cs.new()
i4 = Cs.new()
p Cs.getCount()               # 현재 실행되고있는 인스턴스의 갯수

'''
class Cs:
    count = 0                       # class 변수
    def __init__(self):
        Cs.count = Cs.count + 1     # class이름 . 변수이름
    @classmethod
    def getCount(cls):
        return Cs.count
i1 = Cs()
i2 = Cs()
i3 = Cs()
i4 = Cs()
print(Cs.getCount())

## 클래스 맴버의 추가
'''
# Ruby code ---
class Cal
  attr_reader :v1, :v2
  attr_writer :v1
  @@_history = []
  def initialize(v1,v2)
    @v1 = v1
    @v2 = v2
  end
  def add()
    result = @v1+@v2
    @@_history.push("add : #{@v1}+#{@v2}=#{result}")   # " " 안에서의 변수 인식 = #{ }
    return result
  end
  def subtract()
    result = @v1-@v2
    @@_history.push("subtract : #{@v1}-#{@v2}=#{result}")
    return result
  end
  def setV1(v)
    if v.is_a?(Integer)
      @v1 = v
    end
  end
  def getV1()
    return @v1
  end
  def Cal.history()
    for item in @@_history
      p item
    end
  end
end
class CalMultiply < Cal
  def multiply()
    result = @v1*@v2
    @@_history.push("multipy : #{@v1}*#{@v2}=#{result}")
    return result
  end
end
class CalDivide < CalMultiply
  def divide()
    result = @v1/@v2
    @@_history.push("divide : #{@v1}/#{@v2}=#{result}")
    return result
  end
end
c1 = CalMultiply.new(10,10)
p c1.add()
p c1.multiply()
c2 = CalDivide.new(20, 10)
p c2, c2.add()
p c2, c2.multiply()
p c2, c2.divide()
Cal.history()


'''
class Cal(object):
    _history = []                         # _history를 정의, _는 해당 클래스에서만 사용한다는 의미
    def __init__(self, v1, v2):
        if isinstance(v1, int):
            self.v1 = v1
        if isinstance(v2, int):
            self.v2 = v2
    def add(self):
        result = self.v1+self.v2
        Cal._history.append("add : %d+%d=%d" % (self.v1, self.v2, result))   # history list에 정보 추가
        return result
    def subtract(self):
        result = self.v1-self.v2
        Cal._history.append("subtract : %d-%d=%d" % (self.v1, self.v2, result))
        return result
    def setV1(self, v):
        if isinstance(v, int):
            self.v1 = v
    def getV1(self):
        return self.v1
    @classmethod                                #  클래스 매소드 선언.
    def history(cls):
        for item in Cal._history:              # class 매소드 history에 item을 저장한다. 
            print(item)
class CalMultiply(Cal):
    def multiply(self):
        result = self.v1*self.v2
        Cal._history.append("multiply : %d*%d=%d" % (self.v1, self.v2, result))
        return result
class CalDivide(CalMultiply):
    def divide(self):
        result = self.v1/self.v2
        Cal._history.append("divide : %d/%d=%d" % (self.v1, self.v2, result))
        return result
c1 = CalMultiply(10,10)
print(c1.add())
print(c1.multiply())
c2 = CalDivide(20,10)
print(c2, c2.add())
print(c2, c2.multiply())
print(c2, c2.divide())
Cal.history()