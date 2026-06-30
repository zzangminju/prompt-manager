# 프롬프트 관리 프로그램

def show_menu():
    """메뉴 화면을 보여주는 함수"""
    print("\n===== 프롬프트 관리 프로그램 =====")
    print("0. 종료")
    print("================================")


def main():
    """프로그램을 시작하고 반복시키는 함수"""
    while True:
        show_menu()
        choice = input("번호를 선택하세요: ")

        if choice == "0":
            print("프로그램을 종료합니다. 안녕히 가세요!")
            break
        else:
            print("아직 준비되지 않은 기능이거나 잘못된 번호예요.")


# 프로그램 실행 시작점
main()