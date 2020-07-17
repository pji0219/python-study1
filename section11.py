# Section11
# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MINE - text/csv

# 예제1

import csv
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.reader(f)
    # next(reader) Header 스킵

    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()
    

    for c in reader:
        print(c)

# 예제2

import csv
with open('./resource/sample2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|')
    # next(reader) Header 스킵

    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()
    

    for c in reader:
        print(c)

# 예제3 (Dict변환)

with open('./resource/sample1.csv', 'r') as f:
    reader = csv.DictReader(f)



