# Section11
# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MINE - text/csv

# 예제1

import csv # csv 파일을 사용하기 위해선 파이썬에서 기본적으로 만들어 놓은 csv패키지를 import 시켜줘야 한다.
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.reader(f) # 변수에 reader 함수 선언해서 csv 파일 읽음
    # next(reader) Header 스킵 (맨위 행)

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


# XSL, XLSX(엑셀)
# 엑셀을 처리하는 파이썬 오픈소스: openpyxl, xlsxwriter, xlrd, xlwt, xlutils
# pandas를 주로 사용(왜냐하면 가장 많이 사용하는openpyxl, xlrd를 내부적으로 사용하기 때문)
#1. pip install xlrd 설치
#2. pip install openpyxl 설치
#3. pip install pandas 설치

import pandas as pd

# 옵션 sheetname='시트명' 또는 숫자, header=숫자, skiprow=숫자
xlsx = pd.read_excel('./resource/sample.xlsx')

# 상위 데이터 확인
print(xlsx.head()) # 상위 1~5번째까지 보여줌
print()

# 하위 데이터 확인
print(xlsx.tail()) # 하위 1~5번째까지 보여줌

# 데이터의 행과 열 갯수 확인
print(xlsx.shape)

# 엑셀 or CSV 다시 쓰기
xlsx.to_excel('./resource/result.xlsx', index=False)
# 기존 엑셀 파일의 내용을 위에 쓴 경로에 위 파일명으로 새롭게 파일을 만들어 똑같이 쓰기
# 마지막에 있는 index는 열의 순서를 번호로 매기는건데 False로 하면 순서를 매기지 않음

xlsx.to_csv('./resource/result.csv', index=False)
#위 설명과 동일










