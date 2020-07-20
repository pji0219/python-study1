# Section09
# 파일 읽기, 쓰기
# 읽기 모드 : r, 쓰기 모드(기존 파일 삭제(덮어쓰기)) : w, 추가 모드(파일 생성 또는 추가) : a
#.. : 상대경로, . : 절대경로

# 파일 읽기
# 예제1
f = open('./resource/review.txt', 'r') # 파일을 읽고 쓸때는 항상 open함수를 사용해서 파일의 경로를 적어줘야 한다.
content = f.read() # read라는 함수로 읽어 올수 있다.
print(content)
# 반드시 파일을 읽어 온 다음에는 close로 반환 해야 한다.
f.close()

print("-----------------------------------------------------------------------")

# 예제2
with open('./resource/review.txt', 'r') as f: # with문은 close를 써주지 않아도 자동으로 리소스를 반환 해주기 때문에 편리하다.
    c = f.read()
    print(c)

print("-----------------------------------------------------------------------")

# 예제3

with open('./resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip)

print("-----------------------------------------------------------------------")

# 예제4

with open('./resource/review.txt', 'r') as f:
    content1 = f.read()
    print(">", content1)
    content1 = f.read() # 내용 없음
    print(">", content1)

print("-----------------------------------------------------------------------")

# 예제5

with open('./resource/review.txt', 'r') as f:
    line = f.readline() # 한 줄씩 읽어오기
    # print(line)
    while line:
        print(line, end='#####')
        line = f.readline()

print("-----------------------------------------------------------------------")

# 예제6

with open('./resource/review.txt', 'r') as f:
    content2 = f.readlines # 리스트 형태로 출력
    print(content2)

# 예제7
score = [] # 리스트 형태로 저장
with open('./resource/score.txt', 'r') as f:
    for line in f: # 숫자 한개씩 끝까지 출력
        score.append(int(line)) # txt파일은 문자로 취급 받기에 정수로 형 변환 시켜야 한다.
    print(score)

print('Average : {:6.3}'.format(sum(score)/len(score)))

# 파일 쓰기

# 예제1 파일 쓰기(덮어쓰기)
with open('./resource/text1.txt','w') as w:
    w.write('nice man!\n')

# 예제2(추가 또는 파일 생성)

with open('./resource/text1.txt','a') as a:
    a.write('good man!\n')

# 예제3
from random import randint # 파이썬에서 미리 만들어 놓은 랜덤 패키지의 randint 함수 호출

with open('./resource/text2.txt','w') as w:
    for cnt in range(6):
        w.write(str(randint(1,45)))
        w.write('\n')

# 예제4
# writelines : 리스트 -> 파일로 저장
with open('./resource/text3.txt','w') as w:
    list = ['kim\n', 'park\n', 'cho\n']
    w.writelines(list)

# 예제5
# print문으로 출력하는 것을 파일에 씀
with open('./resource/text4.txt','w') as w:
    print('Test contests1!', file=w)
    print('Test contests2!', file=w)
   