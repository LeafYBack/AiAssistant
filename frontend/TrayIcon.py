import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw
import keyboard
import time

# 创建一个图标的图片
def create_image():
    # 创建一个简单的黑色背景图像
    width = 64
    height = 64
    image = Image.new('RGB', (width, height), color=(0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, width, height), fill=(0, 0, 0))
    return image

# 响应快捷键的函数
def on_hotkey():
    print("快捷键触发！准备与 OneNote 交互...")

# 创建系统托盘菜单
def on_quit(icon, item):
    icon.stop()

# 定义一个功能菜单项
def create_menu():
    return (item('退出', on_quit),)

# 创建托盘图标
def setup_tray():
    icon = pystray.Icon("Test Icon", create_image(), menu=create_menu())
    icon.run()

# 检测快捷键并触发事件
def listen_for_hotkey():
    # 监听快捷键 Ctrl + Shift + A
    keyboard.add_hotkey('ctrl+shift+a', on_hotkey)
    print("正在监听快捷键 Ctrl + Shift + A...")
    
    # 保持程序运行，直到用户按下退出
    while True:
        time.sleep(1)

# 主程序
if __name__ == '__main__':
    # 启动系统托盘图标
    from threading import Thread
    tray_thread = Thread(target=setup_tray)
    tray_thread.daemon = True
    tray_thread.start()
    
    # 启动快捷键监听
    listen_for_hotkey()
