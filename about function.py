# 함수 만들기
# a3()의 이름을 가진 함수 만들기 - a를 3번 출력하는 함수
def a3():
    print('aaa')
a3()


def a4():
    return 'bbb'

print(a4()*3)

def a5():
    print('before')
    return ('ccc')   # 함수 a5()읠 결과 값으로 ccc 를 저장. & 해당 함수(a5()를 종료시킨다
                      # 즉, return 이후의 구문은 실행되지 않는다.
    print('after')    # return뒤에 존재하기에 실행 되지 않는 구문
print(a5())

# 함수에 입력값 적용하기
def a(num):
    print(num)
a(4)

def a_num(num):
    return 'a'*num
print(a_num(8))

# 함수에 여러 입력값 적용하기
def make_string(str, num):
    return str * num
print(make_string('abc', 5))


