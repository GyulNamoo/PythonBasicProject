"""
    함수 : 사용자 정의 함수
    => 한개의 기능을 수행하기 위한 명령문의 집합
       =========
       1. 반복을 제거
       2. 재사용
       3. 구조적인 프로그램 : 단락을 나눠서 처리 => 유지보수, 가독성
    => 함수 종류
       1. 사용자 정의 ***
       2. 라이브러리
    => 함수의 문법
        def 함수명(매개변수):
            명령문 처리
            명령문 처리
        ==================================
                리턴형         매개변수

            def 함수명(매개변수) :
                ...
                ...
                return 한개 => 여러개 전송 가능
                        id,pwd
        ==================================
                 O               O
        ==================================
                 O               X
        ==================================
                 X               O
        ==================================
                 X               X
        ==================================
         매개변수 : default
         def 함수명(매개변수,매개변수=값,매개변수=값):
         print(value,end="\n")
                     =========  default 매개변수
"""
# 리턴형(X), 매개변수(X)
def gugudan():
    for i in range(1,10):
        for j in range(2,10):
            print(f"{j}*{i}={i*j}",end="\t")
        print("")
#gugudan()
"""
    30,40,20,50,10
    == ==           round1
    ==    ==
    20    30
    ==       ==
    20       50
    ==          ==    for 1
    10          20
       == ==          round2
"""
def sort():
    data = [30,40,20,50,10]
    print(f"정렬 전:{data}")
    for i in range(len(data)-1):
        for j in range(i,len(data)):
            if data[i]>data[j]:
                temp = data[i]
                data[i] = data[j]
                data[j] = temp
    print(f"정렬 후 : {data}")
#sort()
# 리턴형(X) 매개변수(O)
"""
def func(매개변수):
    처리  
"""
def find(no):
    data = ["김야옹","치즈냥","신사냥","양말냥","고등어냥"]
    #return data[no]
    print(data[no])
name = find(3)
#print(name)

#리턴형(O), 매개변수(O)
def plus(a,b):
    c = a + b
    return c
def minus(a,b):
    c = a - b
    return c
def gop(a,b):
    c = a * b
    return c
def div(a,b) :
    res = ''
    if b == 0:
        res = '0으로 나눌 수 없다'
    else :
        res = str(a / b)
    return res
a = 10
b = 3
print(plus(a,b))
print(minus(a,b))
print(gop(a,b))
print(div(a,b)) # 정수 / 정수 = 실수

# 매개변수가 default인 경우
"""
    def func(a,b,c)
    def func(a,b=10,c=20)
    
    func(100,200,300) => a=100, b=200, c=300
    func(100) => a=100, b=10, c=20
    func(100,200) => a=100, b=200, c=20
    
    def func(*arg) => 포인트 변수 (가변 매개변수)
    def func(*arg)
    
    func(10)
    func(10,20,30)
    func(10,20,40,50,...)    * , ...
"""
def func(a,b=10,c=20):
    print(f"a={a},b={b},c={c}")
func(100)
func(100,200,300)
func(100,200)

def func(*arg):
    print(arg)
    print(list(arg))
    sum = 0
    for i in arg :
        sum += i
    print(f"총합:{sum}")


#func(1,2,3) #튜플형태로 출력됨
def func_1(a,b):
    print(f"a={a},b={b}")
    c = 0
    try:
        c = a // b
        print(f"c={c}")
    except Exception as e:  #catch(Exception ex)
        print(e)
func_1(10,2)
func_1(10,0)
