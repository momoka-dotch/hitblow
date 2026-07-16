"""難易度選択"""

def select_difficulty():
    while True:
        print("難易度を選んでください")
        print("1 : 易しい（3桁）")
        print("2 : 普通（4桁）")
        print("3 : 難しい（5桁）")

        choice = input("番号 > ").strip()

        if choice == "1":
            return 3
        elif choice == "2":
            return 4
        elif choice == "3":
            return 5
        else:
            print("1～3を入力してください。")
