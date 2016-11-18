'''
모듈: 서로 연관되어 있는 함수들의 모임

import : 모듈을 가져오는 명령어
from xxx import yyyy as zzz  : xxx 모듈중에 yyy 함수를 가져와서 이름을 zzz로 바꾼다.
모듈이름.함수이름 >>> xxx.yyy

- 내장 모듈
- 외장 모듈

'''

import math           # math 모듈을 부러들인다
print(math.ceil(2.1))  # math - 올림값 구하기 : ceil
print(math.floor(2.9)) # math - 내림값 구하기 : floor
print(math.sqrt(32))   # math - 제곱근 구하기 : sqrt


### 모듈안에 객체 담기

# ===========================
# file >>> 1.py
import lib
obj = lib.A()        # class A를  인스턴스화 시켜서 obj로 정의
print(obj.a())


# file >>> lib.py
class A:
    def a(self):
        return 'a'

# ===========================
'''
# ruby code
>>> file.rb
require_relative 'lib'
obj = Lib::A.new()
p obj.a()



>>> file.rb
module Lib
  class A
    def a()
      return 'a'
    end
  end
end



'''