# 프롬프트 관리 프로그램

# 사용할 수 있는 카테고리 목록
categories = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

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
    print("2. 프롬프트 추가")
    print("3. 카테고리별 조회")
    print("4. 검색")
    print("5. 상세 보기")
    print("6. 즐겨찾기 추가/해제")
    print("7. 즐겨찾기 목록")
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


def add_prompt():
    """새 프롬프트를 입력받아 추가하는 함수"""
    print("\n----- 프롬프트 추가 -----")

    title = input("제목: ").strip()
    while title == "":
        print("제목은 비워둘 수 없어요.")
        title = input("제목: ").strip()

    content = input("내용: ").strip()
    while content == "":
        print("내용은 비워둘 수 없어요.")
        content = input("내용: ").strip()

    print("카테고리를 선택하세요:")
    for i in range(len(categories)):
        print(f"  {i + 1}. {categories[i]}")
    category_input = input("번호 또는 직접 입력: ").strip()

    if category_input.isdigit() and 1 <= int(category_input) <= len(categories):
        category = categories[int(category_input) - 1]
    elif category_input == "":
        category = "기타"
    else:
        category = category_input

    prompts.append({
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    })
    print(f"'{title}' 프롬프트가 추가되었어요!")


def show_by_category():
    """카테고리를 선택하면 해당 카테고리의 프롬프트만 보여주는 함수"""
    print("\n----- 카테고리별 조회 -----")
    print("카테고리를 선택하세요:")
    for i in range(len(categories)):
        print(f"  {i + 1}. {categories[i]}")

    choice = input("번호를 선택하세요: ").strip()

    if not (choice.isdigit() and 1 <= int(choice) <= len(categories)):
        print("잘못된 번호예요.")
        return

    selected = categories[int(choice) - 1]

    found = False
    print(f"\n[{selected}] 카테고리 프롬프트:")
    for i in range(len(prompts)):
        if prompts[i]["category"] == selected:
            star = "⭐" if prompts[i]["favorite"] else "  "
            print(f"{i + 1}. {star} {prompts[i]['title']}")
            found = True

    if not found:
        print("이 카테고리에는 프롬프트가 없어요.")


def search_prompt():
    """키워드로 제목이나 내용에서 프롬프트를 검색하는 함수"""
    print("\n----- 프롬프트 검색 -----")
    keyword = input("검색어를 입력하세요: ").strip()

    if keyword == "":
        print("검색어를 입력해야 해요.")
        return

    found = False
    print(f"\n'{keyword}' 검색 결과:")
    for i in range(len(prompts)):
        p = prompts[i]
        if keyword in p["title"] or keyword in p["content"]:
            star = "⭐" if p["favorite"] else "  "
            print(f"{i + 1}. {star} [{p['category']}] {p['title']}")
            found = True

    if not found:
        print("검색 결과가 없어요.")


def show_detail():
    """번호를 입력하면 그 프롬프트의 전체 내용을 보여주는 함수"""
    show_list()

    if len(prompts) == 0:
        return

    choice = input("\n자세히 볼 번호를 입력하세요: ").strip()

    if not (choice.isdigit() and 1 <= int(choice) <= len(prompts)):
        print("잘못된 번호예요.")
        return

    p = prompts[int(choice) - 1]
    star = "⭐ 즐겨찾기" if p["favorite"] else "일반"

    print("\n===== 상세 보기 =====")
    print(f"제목    : {p['title']}")
    print(f"카테고리: {p['category']}")
    print(f"즐겨찾기: {star}")
    print(f"내용    : {p['content']}")
    print("=====================")


def toggle_favorite():
    """번호를 입력하면 즐겨찾기를 켜거나 끄는 함수"""
    show_list()

    if len(prompts) == 0:
        return

    choice = input("\n즐겨찾기를 켜고 끌 번호를 입력하세요: ").strip()

    if not (choice.isdigit() and 1 <= int(choice) <= len(prompts)):
        print("잘못된 번호예요.")
        return

    p = prompts[int(choice) - 1]
    # 현재 상태를 반대로 바꿈 (True면 False, False면 True)
    p["favorite"] = not p["favorite"]

    if p["favorite"]:
        print(f"'{p['title']}'을(를) 즐겨찾기에 추가했어요! ⭐")
    else:
        print(f"'{p['title']}'을(를) 즐겨찾기에서 해제했어요.")


def show_favorites():
    """즐겨찾기한 프롬프트만 모아서 보여주는 함수"""
    print("\n----- 즐겨찾기 목록 -----")

    found = False
    for i in range(len(prompts)):
        if prompts[i]["favorite"]:
            print(f"{i + 1}. ⭐ [{prompts[i]['category']}] {prompts[i]['title']}")
            found = True

    if not found:
        print("즐겨찾기한 프롬프트가 없어요.")


def main():
    """프로그램을 시작하고 반복시키는 함수"""
    while True:
        show_menu()
        choice = input("번호를 선택하세요: ")

        if choice == "1":
            show_list()
        elif choice == "2":
            add_prompt()
        elif choice == "3":
            show_by_category()
        elif choice == "4":
            search_prompt()
        elif choice == "5":
            show_detail()
        elif choice == "6":
            toggle_favorite()
        elif choice == "7":
            show_favorites()
        elif choice == "0":
            print("프로그램을 종료합니다. 안녕히 가세요!")
            break
        else:
            print("잘못된 번호예요. 0부터 7 사이의 번호를 입력해주세요.")


# 프로그램 실행 시작점
main()