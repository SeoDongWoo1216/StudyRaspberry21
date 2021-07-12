
m = 0
n = 1

def func():
    global m  # 전역변수를 사용하기위해 global을 붙여줌
    global n
    m = m + 1
    n += 1

func()
print(m, n)


def counter(max): 
    t = 0

    def output():  # 중첩함수, counter를 호출해야만 사용할 수 있음
        print('t = {0}'.format(t))

    while t < max:
        output()
        t += 1


counter(10)
# output()  # output은 counter에 속하는 함수이기때문에 따로 호출 불가

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(10))
print(factorial(9))
print(factorial(8))
print(factorial(7))
print(factorial(6))
print(factorial(5))
print(factorial(4))


# lambda
a = lambda x , y : x * y
print(a(2, 8))


# closure : 함수 자체를 리턴해줌(대리자)
def calc(a):
    
    def add(b):
        return a+b
    return add

sum = calc(1)
print(sum(2))

@deco
def incre(x):
    return x + 2

def 