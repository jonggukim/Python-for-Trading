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

#============================================


for letter in 'Python':     # 문자열의 반복 출력
   print ('Current Letter :', letter)

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 리스트 데이터터 반복 출력
   print ('Current fruit :', fruit)

print ("Good bye!")

#============================================
# if 와 else 구문을 활용한 loop문 활용
for num in range(10,20):  #to iterate between 10 to 20
   for i in range(2,num): #to iterate on the factors of the number
      if num%i == 0:      #to determine the first factor
         j=num/i          #to calculate the second factor
         print ('%d equals %d * %d' % (num,i,j))
         break #to move to the next number, the #first FOR
   else:                  # else part of the loop
      print (num, 'is a prime number')


# ============================================
# 2 부터 100 까지의 prime number를 구하는 코딩
i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print (i, " is prime")
   i = i + 1

print ("Good bye!")



#============================================
# break
for letter in 'Python':  # 문자열중 해당 문자열까지만 출력하는 코딩
    if letter == 'h':
        break
    print('Current Letter :', letter)




#----------------------------------------
var = 10  # 주어진 값 중 특정값 까지만 반복되는 코딩
while var > 0:
    print('Current variable value :', var)
    var = var - 1
    if var == 5:
        break

print
("Good bye!")

#============================================
# continue
for letter in 'Python':     # 주어진 조건 중 해당 되는 값만 제외 하고 반복 하는 구문 : 문자
   if letter == 'h':        # 문자열"Python"중 "h"만 제외 하고 출력
      continue
   print ('Current Letter :', letter)

#============================================
var = 10                    # 주어진 조건 중 해당 되는 값만 제외 하고 반복 하는 구문 : 정수
while var > 0:
   var = var -1
   if var == 5:             # 문자열"Python"중 "h"만 제외 하고 출력
      continue
   print ('Current variable value :', var)

#============================================
# pass
for letter in 'Python':
   if letter == 'h':         # 주어진 조건 중 해당 되는 값만 제외 하고 반복 하는 구문 : 문자
      pass
      print ('This is pass block')    # 문자열"Python"중 "h"에 해당되면 지정된 구문을 실행하고 다음내용을 출력
   print ('Current Letter :', letter)


#============================================


#============================================


#============================================


















