# 함수

def min(a, b):  # def는 define의 약자
    if (a > b):
        return b
    else:
        return a

c = min(10, 20)
print('10, 20 중에 최소값은 {0}입니다.'.format(c))

##########################################

def printS(c):
    print(c)

printS("Hello")

##########################################

# 여러가지 값을 반환할 수 있음
def divide(a, b):
    return (a/b, a%b)

d, v = divide(20, 4)
print(d, v)
print(type(d)) 
