# section12-2
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 조회

import sqlite3 # sqlite를 사용하기 위한 불러오기

# DB파일 조회(없으면 새로 생성)
conn= sqlite3.connect('/Users/user/Documents/python_basic/resource/database.db')
# 본인 DB 경로

# 커서 바인딩
c = conn.cursor()
# Cursor: 데이터를 읽어오는 만큼 커서가 이동해서 읽어온 위치까지 기억하고 있다가 
# 그 다음 데이터를 읽으면 또 이동 계속해서 읽다가 데이터가 
# 끝나면 읽어올게 없기에 null 또는 none으로 표시

# users 테이블의 데이터를 조회 할 것을 선택
c.execute("SELECT *FROM users")

# 커서 위치가 변경
# 1개 로우 선택
#print('One -> \n', c.fetchone())

# 지정 로우 선택
#print("Three -> \n", c.fetchmany(size=3))
# 여러개 데이터 선택, 3개를 선택 했기에 3개 출력

# 전체 로우 선택
#print('ALL -> \n', c.fetchall())

# 순회 조회

# 순회1
#rows = c.fetchall()
#for row in rows:
    #print('retrieve1 >', row)

# 순회2(보통 이 방법을 주로 사용)
#for row in c.fetchall():
    #print('retrieve2 >', row)

# 순회3(변수로 SQL문을 선언 안하고 직접 for문에 선언)
#for row in c.execute('SELECT * FROM users ORDER BY id desc'):
    #print('retrieve3 >', row)

# 한개만 조회

# WHERE Retrieve1
param1 = (3,) # 튜플 형식으로 변수를 만들어 SQL문에 사용해서 조회
c.execute('SELECT * FROM users WHERE id=?', param1)
# id 3번 데이터만 선택
print('param1',c.fetchone())
# 출력

# WHERE Retrieve2
param2 = 4 #문자열 형식으로 변수를 만들어 SQL문에 사용해서 조회
c.execute('SELECT * FROM users WHERE id="%s"' % param2)
# id 4번 데이터만 선택
print('param2',c.fetchone())
# 출력

# WHERE Retrieve3
c.execute('SELECT * FROM users WHERE id=:Id' ,{"Id": 5})
# id 5번 데이터만 선택, 딕셔너리 형식으로 SQL문 써서 조회
print('param3',c.fetchone())
# 출력

# 여러개 조회

# WHERE Retrieve4
param4 = (3,5)
c.execute("SELECT * FROM users WHERE id IN(?,?)", param4)
# 두개의 id 데이터를 조회하는 SQL문, 변수에 선언된
# id 3,5번 데이터가 ?,?에 매칭 된다.
print('param4',c.fetchall())
# 출력, 여러개를 조회 하기 떄문에 fetchall()을 써야한다.

# WHERE Retrieve5
c.execute("SELECT * FROM users WHERE id IN('%d','%d')" % (3,4))
# 이렇게 변수를 선언 하지 않고 SQL문에 직접 id를 넣어줘서 조회 할수도 
# 있다.
print('param5',c.fetchall())

# WHERE Retrieve6
c.execute("SELECT * FROM users WHERE id=:id1 OR id=:id2",{"id1": 2, "id2": 5})
# 딕셔너리 형식으로 SQL문을 써서 2개의 id를 조회 
print('param6',c.fetchall())



# Dump 출력 (다른 컴퓨터에 똑같은 데이터베이스를 재구성 할때 씀, 즉 백업 용도)

with conn:
    with open('/Users/user/Documents/python_basic/resource/dump.sql','w') as f:
        for line in conn.iterdump(): # dump 할때 쓰는 함수
            f.write('%s\n' % line)
        print('Dump Print Complete')
















