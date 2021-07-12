# 구문 테스트

#initialize
from typing import Coroutine


n = 0

# Loop
# while True:   # 파이썬은 T/F이 대문자임
#     n = n + 1
#     if(n == 100):
#         break
#     # n이 짝수라면 출력할 것
#     if( (n % 2) == 0 ):
#         print(n)

#################################

a = 100 
b = 80

if a > b:
    print('max is {0}'.format(a))
else:
    print('max is {0}',format(b))

i = -45

if i > 0:
    print("{0} is positive".format(i))
elif i == 0:
    print("{0} is zero".format(i))
else:
    print("{0} is negative".format(i))

for u in [0,1,2,3,4]:
    print('{0} * 3 = {1}'.format(u, u*3))

for i in range(5):  # range(5) 는 5까지가 아니고 5 - 1 인 4까지임
    print(i * 2)    # 2 4 6 8 출력

###############################

m = 0
while True:
    m = m + 2
    if (m == 10):   # 10을 생략하고 10 + 2부터 다시 시작함
        continue
    
    if(m == 16):    # 16일때 반복문 종료
        break
    print(m)

for i in range(5):
    pass     # 처리없이 아무것도 안하고 넘어가고 싶을때 사용