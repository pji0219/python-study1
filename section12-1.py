# section12-1
# 파이썬 데이터 베이스  연동(SQLite)
# 테이블 생성 및 삽입

import sqlite3 # sqlite 불러오기 (파이썬에 기본적으로 가지고 있음)
import datetime # 데이터 베이스에 날짜를 삽입하기 위해 불러옴

# 삽입 날짜 생성
now =  datetime.datetime.now()
# 현재 날짜와 시간을 생성 하려면 datetime에 있는 datetime.now 함수를 이용해야한다.
print('now : ', now)# 날짜 출력

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
# 밀리 초를 없애고 싶으면 strftime함수를 이용해서 위와 같이 쓰면 된다.
print('nowDatetime : ',nowDatetime) # 날짜 출력

# sqlite3
print('sqlite3.version:', sqlite3.version) # 버전 확인
print('sqlite3.sqlite_version : ', sqlite3.sqlite_version)# 엔진 버전 확인

# DB 생성 & Auto Commit

conn = sqlite3.connect('C:/Users/user/Documents/python_basic/resource/database.db', isolation_level=None)
# DB를 생성시킬 경로 지정 및 DB생성 맨 뒤에 옵션으로  isolation_level=None 줘야 commit을 안 써줘도 DB에 데이터가 자동 저장 된다.

c = conn.cursor()
print('Cursor Type : ', type(c))
# Cursor: 데이터를 읽어오는 만큼 커서가 이동해서 읽어온 위치까지 기억하고 있다가 
# 그 다음 데이터를 읽으면 또 이동 계속해서 읽다가 데이터가 
# 끝나면 읽어올게 없기에 null 또는 none으로 표시

# 테이블 생성(Data Type : TEXT, INTEGER, REAL, BLOB)

c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, \
email text, phone text, website text, regdate text)")
#execute는 테이블을 만드는 명령어
# 테이블이 없으면 users라는 테이블을 만들겠다는 SQL문이다.
# 그리고 users의 소괄호 안에 있는 것들은 DB에 저장될 목록들의 파일 형식을 지정 해둔것이다.
# 코드가 너무 길어져서 아래 줄에 개행 하기 위해 \를 사용하였다.

# 데이터 삽입

#예제1
c.execute("INSERT INTO users VALUES(1, 'kim', 'kim@naver.com', '010-0000-1234', \
'kim.com', ?)", (nowDatetime,))
# SQL문을 통해 테이블을 만들었을떄 목록들 데이터 형식 순서대로 데이터를 삽입해주면된다.
# 그리고 위에 nowDatetime 변수에 현재 날짜와 시간을 보여주는 함수를 선언했던걸 삽입하려면
# 변수명 그대로 해주게 되면 문자열 그대로 nowDatetime로 삽입 되기에 그러면 안되고
# ?로 처리 해놓고 뒤에 매개 변수로 튜플 형태로 삽입 해줘야한다.
# ? 표는 뒤에 선언된 매개 변수들을 순서대로 매칭 시켜서 삽입 시켜주는데 여기서는
# nowDatetime 한개 밖에 없으니 nowDatetime을 매칭 시켜서 삽입한다.
# 코드가 너무 길어져서 아래 줄에 개행 하기 위해 \를 사용하였다.

# 예제2
c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?,?,?,?,?,?\
)", (2, 'Park', 'Park@daum.net', '010-1111-1111', 'Park.com', nowDatetime,))
# SQL문에 직접 데이터 목록을 써주고 뒤에 데이터 갯수대로 ?를 주고 매개 변수로 데이터를 삽입해줘도 된다.
# 코드가 너무 길어져서 아래 줄에 개행 하기 위해 \를 사용하였다.

# 여러개의 데이터 삽입(튜플 형태와 리스트 형태로)
userList = (
    (3, 'Lee', 'Lee@naver.com', '010-2222-2222', 'Lee.com', nowDatetime),
    (4, 'cho', 'cho@daum.net', '010-3333-3333', 'cho.com', nowDatetime),
    (5, 'Yoo', 'Yoo@google.com', '010-4444-4444', 'Yoo.net', nowDatetime)
)
# 튜플 안의 튜플로 여러 데이터를 저장한다.

c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?,?,?,?,?,?)", userList)
# executemany명령어로 여러개의 데이터를 한꺼번에 삽입 할 수 있다.

# 테이블 데이터 삭제

# 예제1
conn.execute("DELETE FROM users")

# 예제2
print("users db deleted : ", conn.execute("DELETE FROM users").rowcount)
# print문에 테이블 삭제 SQL문을 적어준후 마지막에 .rowcount를 적어주면
#테이블 안의 몇개의 데이터가 지워졌는지 알수있다.

# 커밋: isolation_level = None 일 경우 자동 반영(오토 커밋)
conn.commit()

# 롤백
conn.rollback()

# 접속 해제
conn.close()



