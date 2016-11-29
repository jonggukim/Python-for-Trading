# 구구단을 출력하는 프로그래밍
# ==========================
i=0
def gugu(n):   # 데이터 입력
    result=[]
    i = 1
    while i < 10:
        result.append(n * i)
        i = i +1
    return result

print(gugu(3))

# ==========================
def gugu2(n):
    result = []
    i = 0
    for i in range(1,10):
        result.append(n*i)
    return result
    i = i+1

print(gugu2(4))

# ==========================
gugudan = [
    i*j for i in range(2,10)
                      for j in range(1,10) ]

print(gugudan)

# ==========================
# 구구단 전체를 출력하는 코딩
n=9
m = list(list(range(1*i,(n+1)*i, i)) for i in range(1,n+1))
for i in m:
    i = [str(j).rjust(len(str(m[-1][-1]))+1) for j in i]
    print(''.join(i))


# ==========================
# 특정값을 넣으면 해당 값에대한 구구단을 반환하는 코딩

def input_gugu():
    num = int(input("Display input number's multiplication table: "))
    for i in range (1,11):
        print(num, ' x ', i, '=', num*i )

test = input_gugu()
print(test)

































