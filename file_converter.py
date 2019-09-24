import plugins.csv2excel
import os

# 작업 위치 및 저장 위치 정의
def main():
    input_dir = ""
    print("work dir: " + input_dir)
    output_dir = input_dir + '\\' + "output"

    # input dir 유효성 검사
    if os.path.isdir(input_dir) == 0:
        print("디렉토리를 다시 지정해 주세요")
        exit(0)

    # output 저장 폴더 확인 및 생성
    if os.path.isdir(output_dir) == 0:
        os.mkdir(output_dir)

    files = os.listdir(input_dir)

    #test
