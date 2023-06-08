import subprocess

subprocess.run("adb shell screencap -p /sdcard/screenshot.png")
subprocess.run("adb pull /sdcard/screenshot.png .")
subprocess.run("adb shell rm /sdcard/screenshot.png")
