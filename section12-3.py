# section12-3
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 데이터 수정 및 삭제

import sqlite3

# DB 연결
conn = sqlite3.connect('C:/Users/user/Documents/python_basic/resource/database.db',isolation_level=None)
# 본인의 DB 경로를 지정 및 isolation_level=None 옵션으로 오토 커밋

# Cursor 연결
c = conn.cursor()

# 데이터 수정 방법1
c.execute("UPDATE users SET username = ? WHERE id = ?",('niceman',2))
# ?에 매칭 시켜서 수정

# 데이터 수정 방법2
c.execute("UPDATE users SET username = :name WHERE id = :id",{"name" : 'goodman', "id" : 5})
# 딕셔너리 형태로 써서 수정

# 데이터 수정 방법3
c.execute("UPDATE users SET username = '%s' WHERE id = '%s'" % ('badboy', 3))
# 문자열 형태로 매칭 시켜서 수정


# 중간 데이터 확인1

for user in c.execute("SELECT * FROM users"):
    print(user)


# 데이터 삭제

# 삭제 방법1
c.execute("DELETE FROM users WHERE id = ?", (2,))
# ?에 매칭 시켜서 하는 방법

# 삭제 방법2
c.execute("DELETE FROM users WHERE id = :id", {"id": 5})
# 딕셔너리 형태로 써서 하는 방법

# 삭제 방법3
c.execute("DELETE FROM users WHERE id = '%s'" % (4,))
# 문자열로 매칭 시켜서 하는 방법


# 중간 데이터 확인2

for user1 in c.execute("SELECT * FROM users"):
    print(user1)


# 테이블 전체 데이터 삭제
print("users db deleted : ", conn.execute("DELETE FROM users").rowcount, "rows")
# 마지막에 적어준 .rowcount가 총 삭제된 데이터 개수를 출력해준다.

# 접속 해제
conn.close() # 리소스 반환







