# mixin 은 ruby에서 다중상속의 기능을 한다
'''
# ruby code
module M1
  def m1_m
    p "m1_m"
  end
end
module M2
  def m2_m
    p "m2_m"
  end
end
class C
  include M1, M2     # >>> mixin 기능 M1 과 M2의 기능을 상속 받을때
end
c = C.new()
c.m1_m()
c.m2_m()

# ==================
# mixin의 활용

module Multiply       >>> ruby에서 mixin은 module만 가능하다 class는 불가능.
  def multiply()
    return @v1*@v2
  end
end
module Divide
  def divide()
    return @v1/@v2
  end
end
class Cal
  include Multiply,Divide   # >> module Multiply, Divide의 기능을 상속 받는다.
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
end


c = Cal.new(100,10)
p c.add()
p c.multiply()
p c.divide()










'''