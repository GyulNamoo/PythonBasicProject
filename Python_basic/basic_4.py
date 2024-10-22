"""
    반복문 : while / for => if,for => 데이터 분석
    while 조건 : 조건 True일 때 까지 문장 수행
        실행문장 => while
    실행문장 => 별도의 문장
    ***  ++ , -- : 증감 연산자가 존재하지 않는다
         x++, x--
         x=x+1 , x=x-1
    범위 지정
    초기값 ====== 1
    while 조건: == 2  ==> False면 종료
        실행문장 == 3
        증가식 === 4 ====> 2번 이동
"""
from django.template.defaultfilters import random

i=1
while i<=10 :
    print(f"i={i}", end=" ")
    i=i+1
print("while문 종료")
# 1~10 => 짝수면 출력

i=1
while i<=10:
    if i%2 == 0 :
        print(f"i={i}", end=" ")
    i=i+1
# 1~100 : 합:짝수합, 홀수합
sum = 0
even = 0
odd = 0
i = 1
while i <= 100 :
    sum += i
    if i%2 == 0:
        even = even + i

    else :
        odd = odd + i
    i = i + 1
    print(f"1~100까지의 합:{sum}")
    print(f"1~100까지 홀수의 합:{odd}")
    print(f"1~100까지 짝수의 합:{even}")

    # 들여쓰기 , 기본 문법사항
# import의 위치는 자유롭다 => 자바는 무조건 class위에 존재 ㅎ
import  random
com = random.randrange(1,100)
count = 0
# 무한루프
while True:
    user = int(input("1~100사이의 수를 입력:"))
    count += 1
    if com > user :
        print(f"{user}보다 큰 값 입력:")
    elif com < user :
        print(f"{user}보다 작은 값 입력:")
    else:
        print(f"정답입니다, 입력 횟수는 {count}")
        # 종료 조건 (무한루프는 무조건 종료 조건을 설정 필요) => break
        break


