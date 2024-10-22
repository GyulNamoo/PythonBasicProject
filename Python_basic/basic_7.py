# 리스트형 = List,[]
"""
names = ["하니","해인","혜린","다니엘","민지"]
# 튜플형 = ('하니',20,'한국') => ResultSet => Record
# --- 데이터베이스에서 연동 값 => 튜플로 들어오게 된다 ---
# 셀 = 데이터 중복을 허용하지 않는다
# 변수 = {"사과","배","포도","인삼"}
# 딕트 = {"name":"다니엘","sex":"여자",...} => JSON ... 바로 자바스크립트로 보내서 처리할 수 있다
print(names)
print(names[-1])
for name in names :
    print(name,end=" ")
    print()
# 저장 개수 확인 => len(names)
print(len(names))
print(f"저장개수:{len(names)}")

#추가 => 마지막에 추가 / 원하는 위치에 추가
#       append() extend()    insert()
names.append("대퓨님") # 가장 많이 사용되는 추가 방법
print(names)
names.insert(2,"뉴진스")
print(names)
# 삭제하는 과정 => remove
names.remove("뉴진스")
print(names)
#여러개를 동시에 추가 extend
names.extend(["야옹이","치즈냥"])
print(names)
#뒤에서부터 출력 => reverse
names.reverse()
print(names)

names.sort(reverse=True) # True = DESC , False = ASC
print(names)
"""

arr = [10,20,30,40,50,60,70]
print(arr[0:3])
print(arr[1:3])
print(arr[::])
a = [i for i in range(10)]
print(a)
b = [i for i in range(1,11) if i%2==0]
print(b)
#튜플
"""
    리스트와 비슷 => 변경, 추가, 삭제가 불가능하다 (읽기 전용)
"""
c =(10,20,30)
print(c)
for i in c:
    print(i)
"""
    dict : 키:값을 쌍으로 => 명사:count => JSON
    a = {"키":"값","키":"값"}
"""
dic = {"name":"치즈냥","sex":"수컷","age":7}
# 키가 중복이 된 경우엔 뒤에 설정된 값을 처리 (중복 허용(X))
print(dic)
print(dic['name'])
print(dic['sex'])
print(dic['age'])

# tuple => list로 변경 => list(tuple)
tupleA = {1,2,3}
print(tupleA)
listA = list(tupleA)
print(listA)
tupleB = tuple(listA)
print(listA)
# list => tuple 변경 => tuple(list)
