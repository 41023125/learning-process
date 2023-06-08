from appium import webdriver

# 設置Appium服務
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'device',
    'appPackage': 'com.android.settings',
    'appActivity': '.Settings',
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 監聽點擊事件
while True:
    event = driver.wait_for_event('click')
    x, y = event['x'], event['y']
    print('座標：({0}, {1})'.format(x, y))
