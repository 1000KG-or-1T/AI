import random
import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont

# 更改字体样式
def change_font(widget, font_family, font_size):
    custom_font = tkFont.Font(family=font_family, size=font_size)
    widget.config(font=custom_font)

def get_user_choice(choice):
    global user_choice
    user_choice = choice
    computer_choice = get_computer_choice()
    display_result(user_choice, computer_choice)

def get_computer_choice():
    return random.choice(["剪刀", "石头", "布"])

def determine_winner(user, computer):
    if user == computer:
        return "平局"
    elif (user == "剪刀" and computer == "布") or (user == "石头" and computer == "剪刀") or (user == "布" and computer == "石头"):
        return "你赢了！"
    else:
        return "电脑赢了！"

def display_result(user, computer):
    result = determine_winner(user, computer)
    result_label.config(text=f"你选择了: {user}\n电脑选择了: {computer}\n结果: {result}")
    update_statistics(result)

def update_statistics(result):
    if result == "你赢了！":
        stats["胜利"] += 1
    elif result == "电脑赢了！":
        stats["失败"] += 1
    else:
        stats["平局"] += 1
    
    stats_label.config(text=f"胜利次数: {stats['胜利']}\n失败次数: {stats['失败']}\n平局次数: {stats['平局']}")

def reset_game():
    global stats
    stats = {
        "胜利": 0,
        "失败": 0,
        "平局": 0
    }
    stats_label.config(text=f"胜利次数: {stats['胜利']}\n失败次数: {stats['失败']}\n平局次数: {stats['平局']}")
    result_label.config(text="")
    messagebox.showinfo("游戏提示", "游戏数据已重置！")

def exit_game():
    root.quit()

# 主界面设置
root = tk.Tk()
root.title("剪刀石头布")

# 设置窗口大小为 360x720
root.geometry("360x720")

# 更改字体
custom_font = tkFont.Font(family="宋体", size=16)
root.option_add("*Font", custom_font)

# 用户选择按钮
user_choice = None
frame = tk.Frame(root)
frame.pack(pady=20)

tk.Label(frame, text="请选择你要出的:", font=custom_font).pack()
btn_scissors = tk.Button(frame, text="剪刀", command=lambda: get_user_choice("剪刀"))
btn_stone = tk.Button(frame, text="石头", command=lambda: get_user_choice("石头"))
btn_paper = tk.Button(frame, text="布", command=lambda: get_user_choice("布"))

btn_scissors.pack(side=tk.LEFT, padx=10)
btn_stone.pack(side=tk.LEFT, padx=10)
btn_paper.pack(side=tk.LEFT, padx=10)

# 显示结果框
result_label = tk.Label(root, text="", font=custom_font, pady=20)
result_label.pack()

# 统计结果框
stats = {
    "胜利": 0,
    "失败": 0,
    "平局": 0
}
stats_label = tk.Label(root, text=f"胜利次数: {stats['胜利']}\n失败次数: {stats['失败']}\n平局次数: {stats['平局']}", font=custom_font, pady=20)
stats_label.pack()

# 重置游戏按钮
btn_reset_game = tk.Button(root, text="重置数据", command=reset_game)
btn_reset_game.pack(pady=10)

# 退出按钮
btn_exit_game = tk.Button(root, text="退出", command=exit_game)
btn_exit_game.pack(pady=10)

root.mainloop()