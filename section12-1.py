# section12-1
# 데이터 베이스 연동(sql lite)
# 테이블 생성 및 삽입

import sqlite3
import datetime

# 데이터 삽입 날짜 생성
now = datetime.datetime.now()
print("now :", now)

nowDatetime = now.strftime("%Y-%m-%d %H:%M:%S")
print(nowDatetime)
print()

# sqlite3 버전 확인
print("sqlite3.version :", sqlite3.version)
print("sqlite3.sqlite_version :", sqlite3.sqlite_version)

# DB 생성 & Auto commit
conn = sqlite3.connect("./resource/database.db", isolation_level=None)

# cursor
c = conn.cursor()
print("Cursor type:", type(c))

# 테이블 생성(Data type : TEXT, NUMERIC, INTEGER, REAL, BLOB)
c.execute(
    "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)"
)

# 데이터 삽입 1
# c.execute(
#     "INSERT INTO users VALUES(1, 'KIM', 'kim@naver.com', '010-2222-2222', 'kim.com', ?)",
#     (nowDatetime,),
# )

# 데이터 삽입 2
# c.execute(
#     "INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?,?,?,?,?,?)",
#     (2, "Park", "park@daum.net", "010-4444-9384", "park.com", nowDatetime),
# )

# Many 삽입(튜플, 리스트)
userList = (
    (3, "Lee", "lee@naver.com", "010-2544-1111", "lee.com", nowDatetime),
    (4, "Cho", "cho@naver.com", "010-1255-2344", "cho.com", nowDatetime),
    (5, "Yoo", "yoo@naver.com", "010-4566-4321", "yoo.com", nowDatetime),
)

# c.executemany("INSERT INTO users VALUES(?,?,?,?,?,?)", userList)

# c.executemany(
#     "INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?,?,?,?,?,?)",
#     userList,
# )

# 테이블 데이터 삭제
# conn.execute("DELETE FROM users")
# print("users db delete :", conn.execute("DELETE FROM users").rowcount)

# 커밋 : isolation_level=None 일 경우 자동 반영(오토 커밋)
# conn.commit()

# 롤백
# conn.rollback()

# 접속 해제
conn.close()
