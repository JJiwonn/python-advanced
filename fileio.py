def write_file():
    """
    파일에 텍스트 저장
    : 문장 1개 -> ./sample/test.txt 기록
    : open(파일명, 파일모드, encoding)
    : 액션모드 (r-read:default, w-write, a-append)
    : 형식모드 (t-txt:default, b-binary)
    """
    f = open("./sample/test.txt", "w", encoding="UTF-8")
    write_size = f.write("Life is too short, You need Python")   # 기록한 콘텐츠의 길이
    print("기록된 컨텐츠 길이:", write_size)

def write_file2():
    """
    여러 줄의 -> ./sample/multillines.txt
    """
    f = open("./sample/multilines.txt", "w", encoding="UTF-8")
    for i in range(1, 11):
        f.write(f"Line {i}\n")
    f.close()

def read_file():
    """
    ./sample/multilines.txt 읽어오기
    """
    f = open("./sample/multilines.txt", encoding="UTF-8")
    text = f.read() # 컨텐츠 전체를 읽어옴 -> 파일이 클 경우 과부하
    print(text)
    f.close()

def read_file_by_line():
    """
    줄 단위로 읽어와서 메모리에 부하 줄이기
    """
    f = open("./sample/multilines.txt", "rt", encoding="UTF-8")
    while True:
        line = f.readline() # 한 줄 읽기
        if not line:    # 더 읽어들일 것이 있는가?
            break
        print(line.strip())
    f.close()

def read_file_readlines():
    with open("./sample/multilines.txt", "rt", encoding="UTF-8") as f:
        lines = f.readlines()

        # print(lines)
        for line in lines:
            print(line.strip())

def copy_binary_file():
    """
    이진 파일을 읽거나 쓰기 위해서는 모드를 b로 설정
    : ./sample/rose-flower.jpeg -> ./sample/rose-flower-copy.jpeg로 복사
    """
    # 읽어들이기
    with open("./sample/rose-flower.jpeg", "rb")  as f:
        data = f.read()
        print(type(data), "LENGTH:", len(data))

    # 저장하기
    with open("./sample/rose-flower-copy.jpeg", "wb") as f:
        f.write(data)

    print("파일을 복사했습니다.")

import pickle
def serialize():
    """
    pickle 모듈의 dump 메서드를 이용한 직렬화
    """
    with open("./sample/players.bin", "wb") as f:
        pickle.dump({"baseball", 9}, f, 1)  # dump(객체, 파일포인터, 프로토콜 버전)
        pickle.dump({"basketball", 5}, f, pickle.HIGHEST_PROTOCOL)  # 최신 피클 버전
        pickle.dump({"soccer", 11}, f)  # 위와 동일

    print("직렬화 완료")

def deserialize():
    """
    피클 역직렬화 load, 프로토콜 버전은 명시하지 않아도 됨
    """

    data_list = []

    with open("./sample/players.bin", "rb") as f:
       # print(pickle.load(f))
       # print(pickle.load(f))
       # print(pickle.load(f))
       # print(pickle.load(f))
        while True: # 몇 개인지 모름
            try:
                data = pickle.load(f)
            except EOFError : # 피클이 없음
                break
            data_list.append(data)

    print("역직렬화 결과:", data_list)


"""연습문제
- sample파일 안쪽에 sangbuk.csv파일이용하여
콤마(,)를 기준으로 컬럼 데이터로 되어 있고
이 데이터를 읽어서 콤마를 기준으로 분할 후
한 개 레코드를 dict으로 만들어라
sangbuk.players.bin -> pickle로 dump하기
"""



if __name__ == "__main__":
    # write_file()
    # write_file2()
    # read_file()
    # read_file_by_line()
    # read_file_readlines()
    # copy_binary_file()
    # serialize()
    deserialize()