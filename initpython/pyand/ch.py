import socket
import subprocess
# 設置主機地址和端口號
host = '127.0.0.1'
port = 62001

# 創建套接字對象
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 嘗試連接主機和端口號
result = sock.connect_ex((host, port))

# 檢查連接結果
if result == 0:
    print("端口連接成功！")
else:
    print("端口連接失敗。")
subprocess.run("adb devices")
# 關閉套接字對象
sock.close()
