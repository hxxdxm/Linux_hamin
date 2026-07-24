import random

Q_list  = [
("터미널 창 깔끔하게 정리하는 명령어", "clear"),
("디렉토리 이동 명령어", "cd"),
("디렉토리 만드는 명령어", "mkdir"),
("텍스트 파일을 생성하고 수정하는 명령어", "vi"),
("텍스트 파일을 생성하고 최근 수정 시간을 바꿔주는 명령어", "touch" ),
("상위 디렉토리로 이동하는 명령어", "cd .."),
("디렉토리/파일의 고유한 전체주소 (띄어쓰기X)", "절대경로"),
("현재 작업 중인 파일/디렉토리 기준으로 나타내는 주소 (띄어쓰기X)", "상대경로"),
("현재 디렉토리 안에 있는 모든 파일/디렉토리 자세히 보기", "ls -al")
]

# 문제 맞추기
while True:
    n = 1
    correct = 0
    incorrect = 0
    # 리스트 중에 3개 뽑아서 출제
    selected = random.sample(Q_list, 3)

    # 정답 여부
    for question ,ansewer in selected:
        print(f"문제 {n}:", question)
        user_answer = input("정답을 입력하세요 : ")
        if user_answer.strip().lower() == ansewer:
            correct += 1
            print("정답입니다!\n")
        else :
            incorrect += 1
            print("오답입니다..")
            print(f"정답은 '{ansewer}' 입니다.\n")
        n += 1

    # 등급
    if correct == 3:
        grade = "A"
    elif correct == 2:
        grade = "B"
    elif correct == 1:
        grade = "c"
    else :
        grade = "f"

    #정오 표시 및 등급
    print("정답 수 :", correct)
    print("등급 :", grade)

    # 재시도 여부
    while True:
        yorn = input("\n다시 시도 하시겠습니까?(y/n) :")
        if yorn.lower() == "y":
            print("")
            break
        elif yorn.lower() == "n":
            exit()
        else :
            print("정확한 입력을 해주세요.")