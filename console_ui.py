# console_ui.py

class ConsoleUI:

    
    def show_menu(self):
        print("1. 새 전략 추가")
        print("2. 기존 전략 사용")
        print("3. 종료")

    def get_user_choice(self):
        # 메뉴에서 선택만 받아옵니다.
        while True:
            self.show_menu()
            choice = input("원하는 작업을 선택하세요: ")

            if choice == "1":
                # 새 전략 추가 기능은 추후 구현 예정
                print("새 전략을 추가하는 기능은 추후 추가될 예정입니다.")
            elif choice == "2":
                # 기존 전략 사용
                print("기존 전략을 사용합니다...")
                return "existing"
            elif choice == "3":
                print("종료합니다.")
                return "exit"
            else:
                print("잘못된 입력입니다. 다시 시도하세요.")
