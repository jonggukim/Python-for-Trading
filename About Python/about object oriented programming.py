# about the object oriented programming.
# concept.
'''
ruby code
=====================
name1 = String.new('egoing')  # String is class / name1 is instance of String
name2 = String.new('k8805')
puts(name1.reverse())
puts(name2.reverse())
puts(name1.upcase())
puts(name1.size())
names = Array.new()
names.push('egoing')
names.push('k8805')
puts(names)
puts(names.join(','))

====================================

Object = Class + instance
'''


# 인스턴스 변수의 특성
# python은 methord 외부에서 변수의 접근및 변경을 허용한다.
# 하지만 ruby은 methord 외부에서 변수의 접근및 변경을 불허한다.
class C(object):
    def __init__(self, v):
        self.value = v
    def show(self):
        print(self.value)

c1 = C(10)
print(c1.value)
c1.value = 20
print(c1.value)
c1.show()

'''
### ruby code
class C
  def initialize(v)
    @value = v
  end
  def show()
    p @value
  end
end
c1 = C.new(10)
# p c1.value
# c1.value = 20
c1.show()
'''
## 인스턴스 변수의 접근과 변경 방법 : 메소드를 통한 접근

class C(object):
    def __init__(self, v):
        self.value = v
    def show(self):
        print(self.value)
    def getValue(self):            # 변수의 값 접근
        return self.value
    def setValue(self, v):         # 변수의 값 변경
        self.value = v
c1 = C(10)
print(c1.getValue())
c1.setValue(20)
print(c1.getValue())


'''
### ruby code
class C
  def initialize(v)
    @value = v
  end
  def show()
    p @value
  end
  def getValue()
    return @value
  end
  def setValue(v)
    @value = v
  end
end
c1 = C.new(10)
# p c1.value
p c1.getValue()
# c1.value = 20
c1.setValue(20)
p c1.getValue()
'''

'''

# python origin code.
class Cal(object):                  # 계산기 클래스의 정의
    def __init__(self, v1, v2):      # 인입문
        self.v1 = v1                  # 변수의 정의
        self.v2 = v2

    def add(self):                   # 메소드의 정의 - 더하기
        return self.v1 + self.v2

    def subtract(self):             # 메소드의 정의 - 빼기기
        returnself.v1 - self.v2
'''
class Cal(object):
    def __init__(self, v1, v2):
        if isinstance(v1, int):        # 변수 v1의 값을 숫자로 제한.
            self.v1 = v1
        if isinstance(v2, int):        # 변수 v2의 값을 숫자로 제한.
            self.v2 = v2
    def add(self):
        return self.v1+self.v2
    def subtract(self):
        return self.v1-self.v2
    def setV1(self, v):
        if isinstance(v, int):       # 변수 v2의 값을 숫자로 제한.
            self.v1 = v
    def getV1(self):
        return self.v1
c1 = Cal(10,10)
print(c1.add())
print(c1.subtract())
c1.setV1('one')
c1.v2 = 30
print(c1.add())
print(c1.subtract())


'''
### ruby code
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
    if v.is_a?(Integer)           # 변수 v의 값을 숫자로 제한.
      @v1 = v
    end
  end
  def getV1()
    return @v1
  end
end
c1 = Cal.new(10,10)
p c1.add()
p c1.subtract()
c1.setV1('one')
c1.v1 = 20
p c1.add()
c1.getV1()
'''
# 속성값의 특성 변경 : 변경이 불가능하게 만드는 법 __ >>> __self
class C(object):
    def __init__(self, v):
        self.__value = v
    def show(self):
        print(self.__value)
c1 = C(10)
#print(c1.__value)
c1.show()



'''
### ruby code : 속성값의 특성 변경 _ 변경및 접근이 가능하게 만드는법
class C
  #attr_reader :value
  #attr_writer :value
  attr_accessor :value
  def initialize(v)
    @value = v
  end
  def show()
    p @value
  end
end
c1 = C.new(10)
p c1.value
c1.value = 20
p c1.value

'''