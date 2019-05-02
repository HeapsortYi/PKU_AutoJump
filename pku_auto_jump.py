import os
import subprocess
import time
from io import BytesIO
import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

screenshot_way = 2


def pull_screenshot():  # 获取截图
    global screenshot_way
    if screenshot_way in [1, 2]:
        process = subprocess.Popen(
            'adb shell screencap -p', shell=True, stdout=subprocess.PIPE)
        screenshot = process.stdout.read()
        if screenshot_way == 2:
            binary_screenshot = screenshot.replace(b'\r\n', b'\n')
        else:
            binary_screenshot = screenshot.replace(b'\r\r\n', b'\n')
        return binary_screenshot
    elif screenshot_way == 0:
        os.system('adb shell screencap -p /sdcard/autojump.png')
        os.system('adb pull /sdcard/autojump.png .')


def search(img_jump=None):
    thres1, thres2, thres3 = 255, 210, 62
    if img_jump is None:
        img_jump = cv2.imread('autojump.png')
        thres1, thres3 = thres3, thres1
    # 在右边搜索
    for x in range(1525, 1542):
        for y in range(631, 663):
            if abs(img_jump[x, y, 0] - thres1) <= 1 and abs(img_jump[x, y, 1] - thres2) <= 1 and abs(
                    img_jump[x, y, 2] - thres3) <= 1:
                return True
    return False


def jump(inRight):
    if inRight:
        x, y = 1000, 500
    else:
        x, y = 50, 500
    cmd = 'adb shell input tap {x} {y}'.format(x=x, y=y)
    # print(cmd)
    os.system(cmd)


def run():
    count = 0
    while True:
        count += 1
        print('---\n%-12s %s (%s)' % ('Times:', count, int(time.time())))
        # 获取截图
        binary_screenshot = pull_screenshot()
        img = Image.open(BytesIO(binary_screenshot))
        img = np.array(img)

        inRight = search(img)
        jump(inRight)

        time.sleep(1)
        print('Continue!')


if __name__ == '__main__':
    run()
