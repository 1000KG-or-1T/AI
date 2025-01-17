import random

def get_user_choice():
    print("请选择: 1. 剪刀, 2. 石头, 3. 布")
    choice = int(input("输入你的选择 (1/2/3): "))
    if choice == 1:
        return "剪刀"
    elif choice == 2:
        return "石头"
    elif choice == 3:
        return "布"
    else:
        print("无效的选择，请重新输入。")
        return get_user_choice()

def get_computer_choice():
    return random.choice(["剪刀", "石头", "布"])

def determine_winner(user, computer):
    if user == computer:
        return "平局"
    elif (user == "剪刀" and computer == "布") or (user == "石头" and computer == "剪刀") or (user == "布" and computer == "石头"):
        return "你赢了！"
    else:
        return "电脑赢了！"

def play_game():
    print("欢迎来到剪刀石头布游戏！")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"你选择了: {user_choice}")
    print(f"电脑选择了: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

play_game()
