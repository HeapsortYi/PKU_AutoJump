# PKU_AutoJump
## Introduction
**UPDATE**：更新了使用Chrome浏览器玩的方法，虽然可以跳的更多了，但我的瓶颈似乎就是70多次了。。。
***

用于北大食堂”跳一跳“游戏的辅助程序。仅限安卓手机，调试平台为Windows 10。

参考了[微信跳一跳辅助程序](https://github.com/wangshub/wechat_jump_game)的部分思路和代码。思路为先对游戏界面截屏，然后将图片传到PC端，通过搜索判断下一步应该向左还是向右跳。接着通过adb发出模拟点击命令控制跳动。

尝试了三种截图方法，但是因为速率还是太慢，最多只能跳到21次。。。希望有大佬能解决这个问题

<p align="left"><img src="autojump.png" width = "270" height = "480"/></div>

## Requirements
- 需要下载Adb并配置到系统路径。如果不想下载，可以直接把Tools文件夹下的所有文件复制到根目录也行
- 截图时使用了[uiautomator2](https://github.com/openatx/uiautomator2)，是三种截图方法里最快的。如果不想使用，可以不安装，设置程序里的screenshot_way=0或1即可
- 调试时设置手机屏幕长亮
- 其他import的python库