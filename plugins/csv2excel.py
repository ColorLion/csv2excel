# -*- coding:utf-8 -*-
import openpyxl
import codecs

# dir 내에 있는 csv파일을 excel파일로 변환
# ===============================================
# csv2excel
# parameter
#   - input_dir:    변환할 파일 존재하는 디렉토리
#   - output_dir:   변환된 파일이 저장될 디렉토리
#   - files:        변환할 파일들
# ===============================================
def csv2excel(input_dir, output_dir, files):
    print("input dir: " + input_dir)
    print("output dir: " + output_dir)

    # 폴더 내에 있는 xls 파일을 순차적으로 읽음
    for file in files:
        if len(file.split('.')) == 2:
            if file.split('.')[1] == 'csv':
                print(" - " + file)
                # 파일 형식 지정
                try:
                    # 변환할 CSV 파일 open
                    f = codecs.open(input_dir + file, 'r', encoding='utf8')

                    # 저장할 파일 생성
                    xlsx = openpyxl.Workbook()
                    save = xlsx.active

                    # CSV 데이터 정제
                    for line in f.readlines():
                        save.append(line.replace('"', "").replace("\r\n", "").split(","))

                    # 데이터 저장
                    xlsx.save(output_dir + file.split('.')[0] + ".xlsx")
                except IOError:
                    pass