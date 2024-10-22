# 문자열 제어 / 함수 => 사용자 정의 함수 생성, 오라클 연결
# 크롤링 / 데이터 분석 => Numpy/Pandas/Matplotlib/seaborn
# Django를 이용한 사이트 제작 => React
# 개인 프로젝트 : Spring-Boot / MySql / JPA / ElasticSearch : Spring-Data
# ==> Front => React-Query / Redux ===> 실무 (RestController)
# ==> GET / POST / PUT / DELETE
# ===> NextJS / TypeScript => 본인
# 문자열 함수 = 라이브러리
"""
 문자열
    => 문자 여러개를 저장하는 공간
        '', ""
        예) 'Python' "Python"  => char는 존재하지 않는다
        "Hello Python"
         01234567891011..... index는 0번부터 시작한다
         ** 중간의 일부를 수정할 수 없다 (함수 => 원본은 그대로 유지)
"""
"""
msg ='P'
msg1 = "Python"
print(type(msg))
print(type(msg1))
"""
"""
msg = "Hello Python"
print(msg[0])
for m in msg :
    print(m,end=' ')
print()
"""
"""
# 원하는 문자열의 데이터 추출
ss = "ABCDEFGHIJ"
print(f"ss={ss}") #전체 출력
print(f"ss[0]={ss[0]}") #첫번째 글자 추출 => A
print(f"ss[-1]={ss[-1]}") #마지막 글자 추출 => J
print(f"ss[0:3]={ss[0:3]}") # 0부터 <3R까지 출력
print(f"ss[1:5]={ss[1:5]}")
print(f"ss[-3:-1]={ss[-3:-1]}")
print(f"ss[0:3])={ss[0:3:2]}") # 0 1 2 => A B C => A C
"""
"""
1. upper() = 대문자 변환 => toUpperCase()
2. lower() = 소문자 변환 => toLowerCase()
3. rstrip() lstrip() strip()  => trim()
   공백 제거(오른쪽, 왼쪽,좌 우)
4. _len_() : 문자의 갯수 => len() => length()
5. startswith() : 시작하는 문자열 => startsWith
6. find() : 첫번째 나오는 문자의 번호 추출 => indexOf
7. count() : 문자의 개수 => 그래프 
8. split() : 단어 분리 
9. index() : 해당 위치값 추출
"""
data = " Hello Python "
print(data.upper())
print(data.lower())
print(data.rstrip())
print(data.lstrip())
print(data.strip())
print(data.swapcase()) #대문자 =>소문자, 소문자=>대문자
print(data.__len__())
print(len(data))
print(data.startswith(" H")) # False,True "n"으로 시작한 문자인가?
print(data.find("l")) #"l"의 시작 위치(index번호) 반환
print(data.count("o")) #"o"의 개수 반환
print(data.split(" ")) #" "단위로 나눈다 => [] 배열로 저장
print(data.index('e')) #'e' 위치 반환
