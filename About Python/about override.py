# 재 정의 = override
# 부모객체의 기능을 변경하거나 재 정의 하는 것.
# 부모객체 = 기능1 , 기능2
# 자식객체 = 기능2   >>> 기능2의 재정의

class C1:
    def m(self):
        return 'parent'
class C2(C1):
    def m(self):
#       return  child                    # m()의 리턴값을 child로 변경
        return super().m() + ' child'   # super() >> 부모 class의 m()를 가리킨다. >>>> parent child
    pass                                # 비어있는 매소드를 진행하고자 할때 사용하는 명령어
o = C2()
print(o.m())

'''
# ruby code
class C1
  def m()
    return 'parent'
  end
end
class C2 < C1
  def m()
    return super()+' child'
  end
end
o = C2.new()
p o.m()
'''



# 재 정의의 활용 : 계산기 예제 ==============

# 각 클래스에 info 의 기능을 추가



class Cal(object):
    _history = []

    def __init__(self, v1, v2):
        if isinstance(v1, int):
            self.v1 = v1
        if isinstance(v2, int):
            self.v2 = v2

    def add(self):
        result = self.v1 + self.v2
        Cal._history.append("add : %d+%d=%d" % (self.v1, self.v2, result))
        return result

    def subtract(self):
        result = self.v1 - self.v2
        Cal._history.append("subtract : %d-%d=%d" % (self.v1, self.v2, result))
        return result

    def setV1(self, v):
        if isinstance(v, int):
            self.v1 = v

    def getV1(self):
        return self.v1

    @classmethod
    def history(cls):
        for item in Cal._history:
            print(item)

    def info(self):
        return "Cal => v1 : %d, v2 : %d" % (self.v1, self.v2)


class CalMultiply(Cal):
    def multiply(self):
        result = self.v1 * self.v2
        Cal._history.append("multiply : %d*%d=%d" % (self.v1, self.v2, result))
        return result

    def info(self):
        return "CalMultiply => %s" % super().info()


class CalDivide(CalMultiply):
    def divide(self):
        result = self.v1 / self.v2
        Cal._history.append("divide : %d/%d=%d" % (self.v1, self.v2, result))
        return result

    def info(self):
        return "CalDivide => %s" % super().info()


c0 = Cal(30, 60)
print(c0.info())
c1 = CalMultiply(10, 10)
print(c1.info())
c2 = CalDivide(20, 10)
print(c2.info())


'''
# ruby code ===========
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
    @@_history.push("add : #{@v1}+#{@v2}=#{result}")
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
  def info()
    return "Cal => v1 : #{@v1}, v2 : #{@v2}"
  end
end
class CalMultiply < Cal
  def multiply()
    result = @v1*@v2
    @@_history.push("multipy : #{@v1}*#{@v2}=#{result}")
    return result
  end
  def info()
    return "CalMultiply => #{super()}"
  end
end
class CalDivide < CalMultiply
  def divide()
    result = @v1/@v2
    @@_history.push("divide : #{@v1}/#{@v2}=#{result}")
    return result
  end
  def info()
    return "CalDivide => #{super()}"
  end
end
c0 = Cal.new(30, 60)
p c0.info()
c1 = CalMultiply.new(10, 10)
p c1.info()
c2 = CalDivide.new(20, 10)
p c2.info()


'''