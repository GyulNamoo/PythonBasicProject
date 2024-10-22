import random
# 연산자
"""
    변수 선언 => 출력 / 입력
                print input
        | int , float / bool / str / function도 데이터형으로 처리
        | 데이터가 저장 => 가공(사용자가 요청)
                         ===============
                         연산자 / 제어문
모든 프로그램의 필수 사항 : 변수 설정, 연산자, 제어문

파이썬에서 제공하는 연산자
======================
1. 산술 연산자 : + , - , * , / , %     // , **
   => / (0으로 나눌 수 없다, 정수/정수=실수)
   => + 는 문자열 결합은 없다
           =========
           문자열 + 문자열 (결합 가능)
           문자열 + 정수 (X)
                  => 문자열 변환후에 처리 str(정수)
           문자열 + 실수 (X)
                  => str(실수)
           => print(f"")
           => ** : 10**2 => 제곱근 (10^2)
2. 비교 연산자 : bool
    == , != , < , < , <= , >=  : True/False
            => 조건문, 반복문 처리
3. 논리 연산자 : bool  True / False
    && (X) => and
    ||(X) => or
    !(X) => not
4. 대입 연산자
    =
5. 복합대입 연산자
    += , -= , *= ....
    ======== 누적시에 주로 사용
"""

#문자열 결합
a = "Hello"
b = "홍길동"
print(a+b)
c = 30
print(b+str(c))  #str => 문자열 형변환

print(2**10) #10의 2승 => 100
print(10/3) #실수형
print(10%3)
print(10//3)
# 변수 선언 => return
a,b = 10,20    # a= = 10, b = 20 => 값 여러개 동시에 설정이 가능함 => 함수 return 10,20,30.....
print(f"a={a},b={b}")
c,d = a,b
print(f"c={c},d={d}")
# 산술 연산자
a = 10
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b) # 정수/정수 = 실수
print(a%b)
# 파이썬에만 있는 연산자
print(a**b)
print(a//b) # 정수/정수 = 정수
print("Hello "+"홍길동") #문자열 결합
print("홍길동 "+str(10))
# 형변환
"""
    1. 데이터형 문자열로 변환 : str(변수|값)
    2. True / False로 변경 : bool("True")
                            bool(0)=> False
                            bool(1)=> True : 0이나 0.0이 아니면 True
    3. 실수형 변환 : float()
    4. 정수형 변환 : int() ***** 
"""
print(0.5+float("10")) # 통계 => CSV / 데이터베이스 연동, 웹
print(bool(1),bool(0),bool(0.0),bool(-1))
# 비교연산자 : True / False
a = 10
b = 9
print(a,b)
print(a is b)
print(a==b) #False
print(a!=b) #True
print(a<b) #False
print(a>b) #True
print(a<=b) #False a==b or a<b
print(a>=b) #True  a==b or a>b
# 논리연산자 and or
"""
    조건 and 조건    조건 or 조건 
     |       |       |      | 
     ---------       --------
         |               |
       결과값            결과값
       => and : 범위안에 있는 값
       => or : 범위밖에 있는 값
       
     ------------------------------------------
                      and          or
     ------------------------------------------
     True True       True         True
     -------------------------------------------
     True False      False        True
     -------------------------------------------
     False True      False       True
     -------------------------------------------
     False False     False       False
     -------------------------------------------
     => 제어문 : 조건문 / 반복문
     
     => not : ! (자바)     
"""
a = 10 #True
b = 20 #False
c = 0  #False
print(not(a<b)) #False  not(True) not(False)
print(not(a)) #False
print(not(b)) #False
print(not(c)) #True


# 복합 대입 연산자 += , -=
"""
    x+=1 ===> x=x+1
    x-=1 ==> x=x-1
    
    변수 => 초기화
    1) 명시적 => a = 10
    2) 입력값 => input()
    3) 난수 => random()
"""
# 난수로 초기화
x = random.randrange(1,101)
# 1~100사이의 정수를 추출 (임의로 추출)
y = random.randrange(1,101)
print(f"x={x},y={y}")
print(f"x+y={x+y}")
x+=y
print(f"x+=y={x}")
y-=x
print(f"y-=x={y}")