import curses
import random

# 初始化屏幕
stdscr = curses.initscr()
curses.curs_set(0)  # 隐藏光标
sh, sw = stdscr.getmaxyx()  # 获取屏幕大小
w = curses.newwin(sh, sw, 0, 0)  # 创建一个新窗口
w.keypad(1)  # 开启键盘输入
w.timeout(100)  # 设置刷新时间，单位为毫秒

# 贪吃蛇的初始位置
snake_x = sw // 4
snake_y = sh // 2
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x - 1],
    [snake_y, snake_x - 2]
]

# 食物的初始位置
food = [sh // 2, sw // 2]
w.addch(food[0], food[1], curses.ACS_PI)  # 使用π符号表示食物

# 初始化方向
key = curses.KEY_RIGHT

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key  # 如果没有按键，保持原来的方向

    # 判断蛇是否撞墙或撞到自己
    if snake[0][0] in [0, sh] or \
            snake[0][1] in [0, sw] or \
            snake[0] in snake[1:]:
        curses.endwin()
        quit()

    # 根据当前的方向更新蛇头的位置
    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_DOWN:
        new_head[0] += 1

    # 将新蛇头添加到蛇身
    snake.insert(0, new_head)

    # 如果蛇吃到食物
    if snake[0] == food:
        food = None
        while food is None:
            new_food = [
                random.randint(1, sh - 1),
                random.randint(1, sw - 1)
            ]
            food = new_food if new_food not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()  # 移除蛇尾
        w.addch(tail[0], tail[1], ' ')

    # 更新蛇头
    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
