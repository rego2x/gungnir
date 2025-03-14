'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

options = Options()
# ヘッドレスモード（Linux上で動かすとき必ずこのモードにしておく）
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get('http://www.yahoo.co.jp')
print(driver.current_url)
'''
from selenium import webdriver  
driver = webdriver.Chrome()  
driver.get("https://www.yahoo.co.jp")  
