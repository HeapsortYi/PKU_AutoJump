# coding: utf-8
import time
import pyautogui as pag
import matplotlib.pyplot as plt


def jump(inRight):
    if inRight:
        x, y = 530, 500
    else:
        x, y = 425, 500
    pag.click(x=x, y=y, button='left')


def isInRight():
    # RGB = (255, 210, 62)
    # x, y = 525, 679
    # if pag.pixelMatchesColor(x, y, RGB):
    #     return True
    # return False

    # 分别代表背景色和炸弹的黑色
    RGBs = [(254, 225, 131), (65, 73, 83)]
    x, y = 525, 679
    for rgb in RGBs:
        if pag.pixelMatchesColor(x, y, rgb):
            # print(rgb)
            return False
    return True


def run():
    while True:
        # print('---\n%-12s %s (%s)' % ('Times:', count, int(time.time())))
        inRight = isInRight()
        jump(inRight)

        time.sleep(0.08)
        # print('Continue!')


if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        exit(0)
