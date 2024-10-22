# 한줄 주석
"""
여러줄 주석
1. 파이썬 특징
    1) 데이터형이 존재하지 않는다 (대입값에 따라 결정)
        변수명-값
        a=10
        a="hello"
        a=10.5
        a=true
    2) 특화 ( 주로 사용 )
        웹 : Spring, 데이터 수집, 데이터 분석 : python
            => 파이썬 / 넘파이 / 판다스 / Matplotlib
             Spring + Python (AI)
    3) AI : Back-End, 유지 보수
        => 전송 속도가 빠르다 : Front-End (Vue,React,Next)
            Jquery => Vue, React(금융권,공기업
    4) 파이썬 : 컴파일 없이 인터프리터 (속도가 빠르다)
               배우기가 쉽다, 데이터형 존재 (X) ,
               설정된 변수가 메모리 공간의 이름으로 사용
               모든 데이터는 객체로 인식함 : 메모리 주소를 기억하고 있다
    1. 변수
    2. 연산자
    3. 제어문
    4. 함수
    5. 라이브러리 활용
        => 자료구조가 많음....
        => list형 : [], => 배열 => List
        => 튜플형 => 데이터베이스에서 많이 사용됨 {name:''} : 값이 쌍으로 이루어짐
        => 딕트형 => Map
        => 셀형 => 중복 제거 : Set
    6. 클래스(객체 지향 프로그램)
    7. 데이터베이스
    8. 웹 => 장고 / React
    =====================================================
    프로그램에 필요한 데이터 저장 : 변수, 라이브러리 (배열, 리스트, 딕트...)
        | ==> 사용자 요청에 맞게 데이터 처리
      데이터 처리 ==> 연산자 / 제어문
        |           =============
                         함수 : 중복 제거, 재사용, 구조적인 프로그램
                                                ==============
                                                    | 수정(단락별로)

      처리된 데이터 전송 / 출력
        => ResponseJson(), redirect ....
        => print => \n => \t
    => 저장 : .py, 자바(.java) CSS(.css) JavaScript(.js)
             Vue => CDN(.js), 단독 사용(.vue)
             React (.js,jsx)

    1. 변수
       변경이 가능한 데이터, 메모리에 저장이 된 상태
        ** 휘발성 메모리 보유 (RAM에 저장됨) : 프로그램이 종료시, 자동으로 메모리에서 삭제
        ** 영구적인 저장장치 => File / RDBMS(오라클, MySql)
        ** {}가 없다 => 들여쓰기
        if 조건문 :
        처리 => 오류 발생

        if 조건문 :
         처리
         => 한개의 데이터를 저장하는 공간
    2. 식별자
        1) 알파벳으로 시작(한글 사용이 가능 : 비권장)
        2) 대소문자를 구분
        3) 숫자 사용이 가능 (앞에 사용 금지)
        4) 키워드는 사용이 불가능 => if, for...
        5) 공백을 사용할 수 없다, 특수 문자는 사용이 가능하다 : $, _
    3. 변수 선언 방법
        변수명 = 값
            -- -- 공백 처리 권장
        a=10 => a = 10
        => int / double / bool / string
                           |
                        true / false => 오류
                        True / False
        => 주소값, 데이터형 확인
           =====  ======= type(변수명)
           id(변수명)
"""
# ; 을 사용하지 않는다
a = 10
print(a)
print(id(a))
print(type(a))

b = 10.0
print(b)
print(id(b))
print(type(b))

c = True
print(c)
print(id(c))
print(type(c))

d = "Hello"
print(d)
print(id(d))
print(type(d))

e = 'Hello'
print(e)
print(id(e))
print(type(e))

print("a는 %d이다" %a)
b = 10
c = 20.0
d = "홍길동"
print("b:{},c:{},d:{}".format(b,c,d))
print(f"=%d,c=%f,d=%s")
print(f"b={b},c={c},d={d}") #SQL
# select * from emp where empno={empno}
m = 3
n = 3
print(id(m),id(n))
# 변수가 같은 값을 가지고 있는 경우에는 주소가 동일하다...!!
print(m is n) #bool로 처리된다

k = 1
o = 2
print(f"k={k}",end="Hello\t") # 특수문자 (\n => 변경이 가능)
#print의 기본은 \n이 붙어있음... => 변경시에는 end="\t"  \t : tab end="" : 붙여쓰기
a1 = 1
a2 = 2
a3 = 3
print("a1:{},a2:{},a3:{}".format(a1,a2,a3),sep="-")
print("name:%s" %"Hello")
print("age:%d" %20)
print("key:%f" %180.12)

#입력받는 형식
print("이름 입력:")
name = input()
print(f"name={name}")

#  멀티 라인
data = """안녕하세요 고양이 입니다
나이는 30세 입니다"""
print(data)