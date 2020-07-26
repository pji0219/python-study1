# section13-2
# 업그레이드 타이핑 게임 제작
# 타이핑 게임 제작 및 기본 완성

import random # 랜덤으로 단어를 가져오기 위해 패키지 호출
import time # 게임 하는데 걸린 시간을 가져오기 위해 패키지 호출
import winsound # 사운드 출력 모듈
import sqlite3
import datetime

# DB 생성 & 오토 커밋
conn = sqlite3.connect('C:/Users/user/Documents/python_basic/resource/records.db', isolation_level=None)
# 커서 연결
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS records(id INTEGER PRIMARY KEY AUTOINCREMENT, cor_cnt INTEGER, record text, regdate text)")



words = [] # 영어 단어 리스트(1000개 로드)

n = 1 # 게임 시도 횟수
cor_cnt = 0 # 정답 개수

with open('./resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip())
        # 반복문과 word.txt 파일의 단어들을 append함수를 통해 
        # words변수에 선어된 리스트에 추가
        # 그리고 strip()함수를 통해 혹시 모를 단어에 있을 공백 제거
        # (공백이 있는 단어와 없는 단어는 서로 다른것으로 취급하기에)


input("Ready? Press Enter Key!") 
# 사용자가 입력하기 전까지는 대기 하고 있다가
# 입력 후 작동
start = time.time()

while n <= 5: # 단어를 5개 나오게 하기위해 5번이하까지 조건줌
    random.shuffle(words) # words에 있는 단어들을 섞어줌
    q = random.choice(words)
    # 섞인 단어중에 하나를 뽑아옴

    print()

    print("*Question # {}".format(n))
    # 포맷 함수에 n을 주었기 때문에 5번 출력
    print(q) # 문제 출력

    x = input() # 타이핑 입력

    print()

    if str(q).strip() == str(x).strip(): # 입력 확인 (공백 제거)
        print("Pass!")
        # 정답 소리 재생
        winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)

        cor_cnt += 1
    else:
        # 오답 소리 재생
        winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)


        print("Wrong!")
    n += 1 # n에 숫자를 1씩 증가 시키기 위한 것(다음 문제 전환)

end = time.time() # End Time
et = end - start # 총 게임 시간
et = format(et, ".3f") # 소수점 3째자리 까지 출력(시간)

if cor_cnt >= 3:
    print("합격")
else:
    print("불합격")

# 기록 DB 삽입
cursor.execute("INSERT INTO records('cor_cnt', 'record', 'regdate') VALUES(?, ?, ?)", (cor_cnt, et, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

# 수행 시간 출력
print("게임 시간 : ", et, "초", "정답 개수 : {}".format(cor_cnt))

# 시작 지점 코드
if __name__ == '__main__':
    pass










