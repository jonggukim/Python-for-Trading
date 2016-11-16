'''
*** home work : crate the code for printing below lines

print("Hello world 0")
print("Hello world 9")
print("Hello world 18")
print("Hello world 27")
print("Hello world 36")
print("Hello world 45")
print("Hello world 54")
print("Hello world 63")
print("Hello world 72")
print("Hello world 81")

'''


# way 1: use while

i = 0
while i < 10:   # 반복 조건
    print("Hello Workd for while " + str(i*9))
    i = i + 1

'''
while True:  <<<무한 루프
    print("results)

>>>> results를 무한출력.

'''
members = ['egoing', 'leezche', 'graphittie','222','ㅁㄴㅇㄹㄴㄷㄹ']
i = 0
while i < len(members):  # list members의 값 만큼 반복 >> 변화에 적응
    print(members[i])     # list 중 i 값 만큼 실행
    i = i + 1


# way 1: use for
'''
for i in x:  X = 컨테이너(리스트,듀플,딕셔너리 등등)의 값을 i 에 대입한다.
  print(i)
>>>

'''

a = 0
for a in range (10):  # 반복 조건
    print('hello world  '+ str(a*9))
    a = a + 1