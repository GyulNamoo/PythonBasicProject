"""
    제어문
    1. 조건문
        = 단일 조건문
          if 조건문:
            처리문장 = 조건문이 True일 경우에만 처리가 된다
          ========= 들여쓰기 주의
        = 선택 조건문
          if 조건문:
            처리문장 => 조건이 True 일 때
          else:
            처리문장 => 조건이 False일 때
        = 다중 조건문 => 조건에 맞는 if만 처리가 된다
          if 조건문 :
            처리문장 => True : 문장을 수행 종료
          elif 조건문:
            처리문장 => True : 문장을 수행 종료
          elif 조건문:
            처리문장
          ...                    ....
          else :
            처리문장 => True값이 없을 때 수행후 종료
    2. 반복문
        = while
        = for
    3. 반복제어문
        = continue
        = break
"""
import  random
#조건문
x = random.randrange(1,101)
print(f"x={x}")
if x%2 == 0 :
    print(f"{x}는 짝수이다")  # if문 소속
elif x>=50:
    print(f"{x}는 50 이상 홀수이다")
else:
    print(f"{x}는 50 이하 홀수다")
print("프로그램 종료") # 별도의 문장

# 실행 문장이 두개이상인 경우
if x%2==0:
    print("if문 수행")
    print(f"{x}(은)는 짝수이다")
else:
    print("else문 실행")
    print(f"{x}(은)는 홀수이다")

#============ 응용 ==============
com = random.randrange(0,3) #0,1,2
user = int(input("가위(0),바위(1),보(2):"))# str 문자열
print(type(com),type(user))
"""
    중첩 조건문
    com = 가위(0)     => 9가지 경우
        user = 가위
               바위
               보
"""
if com == 0:
    print("컴퓨터:가위")
    if user == 0:
        print("사용자:가위")
        print("비겼다")
    elif user == 1:
        print("사용자:바위")
        print("이겼다")
    elif user == 2:
        print("사용자:보")
        print("졌다")
elif com == 1:
    print("컴퓨터:바위")
    if user == 0:
        print("사용자:가위")
        print("비겼다")
    elif user == 1:
        print("사용자:바위")
        print("이겼다")
    elif user == 2:
        print("사용자:보")
        print("졌다")
elif com == 2:
    print("컴퓨터:보")
    if user == 0:
        print("사용자:가위")
        print("비겼다")
    elif user == 1:
        print("사용자:바위")
        print("이겼다")
    elif user == 2:
        print("사용자:보")
        print("졌다")

