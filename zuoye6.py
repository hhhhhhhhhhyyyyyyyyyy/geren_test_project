from selenium import webdriver

# 初始化 Edge 浏览器，Selenium 会自动处理驱动
driver = webdriver.Edge()

# 打开百度页面
driver.get("https://www.baidu.com")

# 打印页面标题，验证是否成功打开
print("当前页面标题：", driver.title)

# 关闭浏览器
driver.quit()