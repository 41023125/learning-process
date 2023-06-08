import subprocess


def click(x, y):
    subprocess.run(['adb', 'shell', f'input tap {x} {y}'])


click(106, 107)  # 點擊座標 (500, 500)
