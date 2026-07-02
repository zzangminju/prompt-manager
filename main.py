# 프롬프트 관리 프로그램

# 기본 프롬프트 데이터 (프로그램 시작 시 미리 등록됨)
prompts = [
    {
        "title": "블로그 글 작성",
        "content": "다음 주제로 친근한 말투의 블로그 글을 800자 내외로 써줘. 주제: ",
        "category": "텍스트 생성",
        "favorite": False
    },
    {
        "title": "고양이 일러스트",
        "content": "귀여운 흰색 고양이가 창가에서 햇볕을 쬐는 모습, 따뜻한 파스텔 톤, 수채화 스타일",
        "category": "이미지 생성",
        "favorite": True
    },
    {
        "title": "친절한 상담원 페르소나",
        "content": "너는 친절하고 인내심 많은 고객 상담원이야. 항상 공손한 존댓말로 답하고, 어려운 용어는 쉽게 풀어서 설명해줘.",
        "category": "페르소나",
        "favorite": False
    },
]


def show_menu():
    """메뉴 화면을 보여주는 함수"""
    print("\n===== 프롬프트 관리 프로그램 =====")
    print("1. 전체 목록 보기")
    print("0. 종료")
    print("================================")


def show_list():
    """저장된 모든 프롬프트를 번호와 함께 보여주는 함수"""
    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return

    print("\n----- 프롬프트 목록 -----")
    for i in range(len(prompts)):
        p = prompts[i]
        star = "⭐" if p["favorite"] else "  "
        print(f"{i + 1}. {star} [{p['category']}] {p['title']}")


def main():
    """프로그램을 시작하고 반복시키는 함수"""
    while True:
        show_menu()
        choice = input("번호를 선택하세요: ")

        if choice == "1":
            show_list()
        elif choice == "0":
            print("프로그램을 종료합니다. 안녕히 가세요!")
            break
        else:
            print("아직 준비되지 않은 기능이거나 잘못된 번호예요.")


# 프로그램 실행 시작점
main()