## 문자와 파이선

#첫 번째 문자의 대문자 출력 : hello --> Hello
print('hello world'.capitalize())
# >>> Hello world

#문자열을 대문자로 변환 : upper()
print('hello world'.upper())
# >>> HELLO WORLD

#문자열의 갯수를 정수로 표현: __len__() or len()
#1-way
print('hello world'.__len__())
#2-way
print(len('hello world'))
#>>> 11

#문자열의 변환 혹은 교체: replace('바꿀 문자','바뀔 문자')
print('hello world'.replace('world', 'programing study'))
#>>> hello world >> hello programing study

a= 'hello world'
print(a)
print(a.replace('world', 'test replace'))

#특수 문자들:
# escape simbal - back slash \" >> 기호를 문자로 표현할때.
# " your name's "tutorial" "

print(" your name's \"tutorial\" ")
print("\\")

# 줄바꿈: \n
print('hello \nworld')
print("hello \nworld")
'''
hello
world
'''

#들여쓰기: \t
print('hello \tworld')
# >>> hello    world

