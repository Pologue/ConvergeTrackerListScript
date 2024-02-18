#!/e/Anaconda/python
import os
import time
import pyperclip as clip
import pyautogui as gui

# add links
links = []
# https://github.com/ngosang/trackerslist
links.append("https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best.txt")
links.append("https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt")
links.append("https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_udp.txt")
links.append("https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_http.txt")
links.append("https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_https.txt")
links.append("https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_ws.txt")
links.append("https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best_ip.txt")
links.append("https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_ip.txt")

# download links by curl to tracker.txt
os.system("del tracker.txt")
# date = time.strftime("%Y-%m-%d", time.localtime())
commands = ["curl -ks " + link + " >> tracker.txt" for link in links]
total = len(commands) * 1.0
success = 0.0
for command in commands:
    respond = os.system(command)
    if (respond == 0):
        print('Success\n')
        success += 1
    else:
        print('Fatal\n')
print(f'{success / total * 100}% commands successed')

# copy from tracker.txt
tracker = ""
with open("tracker.txt") as file:
    tracker = file.read()
clip.copy(tracker)

# gui operation
# ! not recommended
# * run below when qBittorrent's window is closed
# gui.mouseInfo()
""" gui.moveTo(1599, 1599)
time.sleep(1)
gui.click(2043, 1567)
time.sleep(1)
gui.click(1926, 1350)
time.sleep(1)
gui.click(935, 437)
time.sleep(1)
gui.click(856, 774)
time.sleep(1)
gui.moveTo(1556, 828)
time.sleep(1)
gui.scroll(-1000)
time.sleep(1)
gui.click(1608, 1072)
time.sleep(1)
gui.hotkey('ctrl', 'a')
time.sleep(1)
gui.hotkey('ctrl', 'v')
time.sleep(1)
gui.click(1603, 1192) """
