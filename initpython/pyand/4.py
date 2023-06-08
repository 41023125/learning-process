import subprocess

# 模擬在模擬器屏幕上按下1鍵
subprocess.run(["adb", "shell", "input", "keyevent", "8"])
