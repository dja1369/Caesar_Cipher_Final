import Caesar
#Caesar에 있는 아스키아트 출력
print(Caesar.logo)
#While문을 위한 변수
app_continue = True
#app_continue가 True 일 동안 반복.
while app_continue:
    #암호화할지 해독할지 입력받기
    type = input("encode 는 암호화 , decode 는 해독화 입니다 둘중하나를 선택하여 주세요:\n").lower()
    # 텍스트를 입력받고 대소문자의 구분을 없애기 위해 전부 소문자로 변환하여 저장
    text = input("텍스트를 입력하세요(영어로) :\n").lower()
    # 이동할 숫자를 문자열로 입력받고 정수형으로 변환
    # 넘길 숫자가 배열 크기를 초과할 경우를 대비하여 26개인 알파벳의 나머지를 받아서 범위를 제한
    shift = int(input("넘어갈 숫자를 입력하세요 :\n"))
    shift = shift % 26

    # 암호화 및 해독 하는 코드 정의
    def Caesar_cipher(insert_text, insert_shift, insert_type):
        #문자를 입력받기위한 빈 문자열 선언
        cipher_text = ""
        #암호화를 선택하면 shift 에 -를 곱하여 역순으로 변경
        if insert_type == "decode":
            insert_shift *= -1
        #반복문 을 입력받은 텍스트 만큼 반복하기
        for char in insert_text:
            #문자가 알파벳 리스트에 있다면 인덱스를 참조하여 새로운 문자를 빈 문자열에 추가
            #문자가 알파벳 리스트에 없다면 그대로 빈 문자열에 추가
            if char in Caesar.alphabet:
                position = Caesar.alphabet.index(char)
                new_position = position + insert_shift
                new_word = Caesar.alphabet[new_position]
                cipher_text += new_word
            elif char not in Caesar.alphabet:
                cipher_text += char
        print(f"{insert_text}는 {cipher_text} 입니다.")

    Caesar_cipher(insert_type=type, insert_text=text, insert_shift=shift)
    #모든 과정을 거치고 재시작 할건지 입력받음
    #만약 N를 입력한다면 app_continue 를 False 로 변경하여 While문 종료.
    result = input("Y를 누르시면 재시작 , N을 누르시면 종료 입니다.").lower()
    if result == "n":
        app_continue = False
