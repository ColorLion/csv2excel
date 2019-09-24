import plugins.csv2excel
import plugins.excel2csv
import os

# 작업 위치 및 저장 위치 정의
def main():
    # 작업 위치를 입력 받음
    input_dir = input("dir: ")
    print("work dir: " + input_dir)

    # input dir 유효성 검사
    if os.path.isdir(input_dir) == 0:
        print("디렉토리를 다시 지정해 주세요")
        exit(0)

    # 변환하고자 하는 파일의 확장자 확인
    # 추후 변경(플러그인에서 변경)
    print("convert 지원하는 확장자: csv to excel, excel to csv")

    # 추후 변경(optparse 사용)
    src_ext = input("source file extension: ")
    dst_ext = input("destination file extension: ")
    ext = src_ext + "2" + dst_ext

    # 변환하는 확장자의 유효성 검사
    # 이것도 어떻게 해결해보자고
    if ext == "csv2excel" or ext == "excel2csv":
        pass
    else:
        print("변환하려는 확장자가 잘못되었거나 지원하지 않습니다")

    # output 저장 폴더 확인 및 생성
    output_dir = input_dir + '\\' + "output"
    if os.path.isdir(output_dir) == 0:
        os.mkdir(output_dir)

    # 변환 함수 사용
    if ext == "csv2excel":
        print("csv2excel")
    elif ext == "excel2csv":
        print("excel2csv")
    else:
        print("이게 출력되면 안되긴 함")