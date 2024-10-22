import oracledb
def getConnection():
    try:
        conn = oracledb.connect(user="hr",password="happy",dsn="localhost:1521/XE")
    except Exception as e:
        print(e)

    return conn
def foodListData(page):
    conn = getConnection()
    cursor = conn.cursor() #ps = conn.preparedStatement()
    rowSize = 20
    start = (rowSize*page)-(rowSize-1)
    end = rowSize * page

    #SQL문장
    sql = f"""
            SELECT fno,name,address,num
            FROM (SELECT fno,name,address,rownum as num
                  FROM(SELECT fno,name,address
                       FROM project_food_house ORDER BY fno ASC))
            WHERE num BETWEEN {start} AND {end} 
           """
    cursor.execute(sql) #ps.execute()

    food_list = cursor.fetchall()
    # 튜플형태로 받는다 () => [(),(),()]
    # selectList - selectOne
    # fetchAll - fetchOne
    cursor.close()
    conn.close()
    return food_list

def foodTotalPage():
    conn = getConnection()
    cursor = conn.cursor()
    sql = """
            SELECT CEIL(COUNT(*)/20.0)
            FROM project_food_house
          """ #멀티라인
    cursor.execute(sql)
    total=cursor.fetchone()[0] #fetchOne() 은 항상 튜플만 반환한다 => [0]으로 숫자만 출력
    cursor.close()
    conn.close()
    return total

food_list = foodListData(1)
print(food_list)
total = foodTotalPage()
print(total)