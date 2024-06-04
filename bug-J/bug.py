#import pyautogui
import random
import tkinter as tk
import threading
import win32api
import time
import psutil

from win32api import GetMonitorInfo, MonitorFromPoint
window = tk.Tk()
screen_width = window.winfo_screenwidth()
x = screen_width - 100
cycle = 0
check = 1
idle_num = [1, 2]
sleep_num = [10,11,12, 13, 15]
walk_left = [3,6, 7]
walk_right = [4,8, 9]
event_number = random.randrange(1, 3, 1)

monitor_info = GetMonitorInfo(MonitorFromPoint((0,0)))
monitor_area = monitor_info.get("Monitor")
work_area = monitor_info.get("Work")
print("The taskbar height is {}.".format(monitor_area[3]-work_area[3]))
taskbar_height= monitor_area[3]-work_area[3]
print(work_area[3])#1050
def dupe_myself():
    win32api.ShellExecute(0,'open','bug.exe',"",'',0)

def schedule_dupe():
    # 随机选择时间
    time_to_wait = random.randint(114514, 480000)  # 、time to ms
    window.after(time_to_wait, lambda: threading.Thread(target=dupe_myself).start())
    # 再次调用schedule_dupe以循环此过程
    window.after(time_to_wait, schedule_dupe)

def kill_process_by_name(process_name):
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process_name:
            proc.kill()

def schedule_kill():
    # 随机选择时间
    time_to_wait = random.randint(114514, 480000)  # 、time to ms
    window.after(time_to_wait, lambda: threading.Thread(target=kill_process_by_name('bug.exe')).start())
    # 再次调用schedule_dupe以循环此过程
    window.after(time_to_wait, schedule_kill)
# 示例使用
# kill_process_by_name('bug.exe')

schedule_dupe()
schedule_kill()
# transfer random no. to event
def event(cycle, check, event_number, x):
    if event_number in idle_num:
        check = 0
        print('idle')
        window.after(400, update, cycle, check, event_number, x)  # no. 1,2,3,4 = idle

    elif event_number == 5:
        check = 1
        print('from idle to sleep')
        window.after(100, update, cycle, check, event_number, x)  # no. 5 = idle to sleep
    elif event_number in walk_left:
        check = 4
        print('walking towards left')
        window.after(100, update, cycle, check, event_number, x)  # no. 6,7 = walk towards left
    elif event_number in walk_right:
        check = 5
        print('walking towards right')
        window.after(100, update, cycle, check, event_number, x)  # no 8,9 = walk towards right
    elif event_number in sleep_num:
        check = 2
        print('sleep')
        window.after(1000, update, cycle, check, event_number, x)  # no. 10,11,12,13,15 = sleep
    elif event_number == 14:
        check = 3
        print('from sleep to idle')
        window.after(100, update, cycle, check, event_number, x)  # no. 15 = sleep to idle

# making gif work
def gif_work(cycle, frames, event_number, first_num, last_num):
    if cycle < len(frames) - 1:
        cycle += 1
    else:
        cycle = 0
        event_number = random.randrange(first_num, last_num + 1, 1)
    return cycle, event_number


def update(cycle, check, event_number, x):
    # idle
    if check == 0:
        frame = idle[cycle]
        cycle, event_number = gif_work(cycle, idle, event_number, 1, 9)

    # idle to sleep
    elif check == 1:
        frame = idle_to_sleep[cycle]
        cycle, event_number = gif_work(cycle, idle_to_sleep, event_number, 10, 10)
    # sleep
    elif check == 2:
        frame = sleep[cycle]
        cycle, event_number = gif_work(cycle, sleep, event_number, 10, 15)
    # sleep to idle
    elif check == 3:
        frame = sleep_to_idle[cycle]
        cycle, event_number = gif_work(cycle, sleep_to_idle, event_number, 1, 1)
    # walk toward left
    elif check == 4:
        frame = walk_positive[cycle]
        cycle, event_number = gif_work(cycle, walk_positive, event_number, 1, 9)
        x -= 3
        if x < 0:  # 如果超出窗口最左边
            x = 0
            check = 5  # 反方向行走
    # walk towards right
    elif check == 5:
        frame = walk_negative[cycle]
        cycle, event_number = gif_work(cycle, walk_negative, event_number, 1, 9)
        x += 3
        if x > window.winfo_screenwidth() - 100:  # 如果超出窗口最右边
            x = window.winfo_screenwidth() - 100
            check = 4  # 反方向行走

    screen_height = window.winfo_screenheight()

    # 设置窗口位置
    window.geometry('20x20+' + str(x) + '+' + str(screen_height-20-taskbar_height))
    # window.geometry('100x100+'+str(x)+'+716')#啊呀这个屎山堆
    label.configure(image=frame)
    window.after(1, event, cycle, check, event_number, x)
    print(screen_height)#1080



# window = tk.Tk()
# call buddy's action gif
idle = [tk.PhotoImage( file = 'idle.gif', format='gif -index %i' % (i)) for i in range(5)]  # idle gif
idle_to_sleep = [tk.PhotoImage(file='idle_to_sleep.gif', format='gif -index %i' % (i)) for i in
                 range(8)]  # idle to sleep gif
sleep = [tk.PhotoImage(file='sleep.gif', format='gif -index %i' % (i)) for i in range(3)]  # sleep gif
sleep_to_idle = [tk.PhotoImage( file='sleep_to_idle.gif', format='gif -index %i' % (i)) for i in
                 range(8)]  # sleep to idle gif
walk_positive = [tk.PhotoImage(file='walking_positive.gif', format='gif -index %i' % (i)) for i in
                 range(8)]  # walk to left gif
walk_negative = [tk.PhotoImage( file='walking_negative.gif', format='gif -index %i' % (i)) for i in
                 range(8)]  # walk to right gif
# window configuration
window.config(highlightbackground='black')
label = tk.Label(window, bd=0, bg='black')
window.overrideredirect(True)
window.wm_attributes('-transparentcolor', 'black')
window.wm_attributes('-topmost', 1)  # 确保窗口始终在顶部
label.pack()
# loop the program
window.after(1, update, cycle, check, event_number, x)
window.mainloop()

# 创建事件，使执行5min后自动退出