# coding: utf-8
import os
import subprocess
import time
from io import BytesIO
import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

screenshot_way = 2


def pull_screenshot():  # 获取截图。screenshot_way分别对应3种截图方式，从高到低越来越慢
    global screenshot_way
    if screenshot_way == 2:
        # 在使用时需要将devices_ip换成自己设备的，可以通过adb devices命令查看
        os.system(
            'python -m uiautomator2 screenshot {devices_ip} autojump.jpg'.format(
                devices_ip='xxxxxxxxxxxx'))
        return None
    elif screenshot_way == 1:
        process = subprocess.Popen(
            'adb shell screencap -p', shell=True, stdout=subprocess.PIPE)
        screenshot = process.stdout.read()
        binary_screenshot = screenshot.replace(b'\r\n', b'\n')

        return binary_screenshot
    elif screenshot_way == 0:
        os.system('adb shell screencap -p /sdcard/autojump.jpg')
        os.system('adb pull /sdcard/autojump.jpg .')
        return None


def search(img_jump=None):
    R, G, B = 255, 210, 62

    if img_jump is None:
        img_jump = cv2.imread('autojump.jpg')
        R, B = B, R
    else:
        img_jump = Image.open(BytesIO(img_jump))
        img_jump = np.array(img_jump)

    # 经过观察发现包子的坐标是固定不变的，那么只要在右边某个固定的范围搜索有没有出现橘色的点即可。
    # 如果出现，则向右跳；否则，向左跳
    for x in range(1525, 1542):
        for y in range(631, 663):
            if abs(img_jump[x, y, 0] - R) <= 2 and abs(img_jump[x, y, 1] - G) <= 2 and abs(
                    img_jump[x, y, 2] - B) <= 2:
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
        screenshot = pull_screenshot()
        inRight = search(screenshot)
        jump(inRight)

        # time.sleep(1)
        print('Continue!')


if __name__ == '__main__':
    run()
