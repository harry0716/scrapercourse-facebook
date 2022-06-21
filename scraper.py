from selenium import webdriver  #載入瀏覽器驅動模組
from webdriver_manager.chrome import ChromeDriverManager  #載入瀏覽器驅動模組管理員，匯入chrome驅動程式管理員
from selenium.webdriver.common.by import By       #載入定位模組
import time   #載入時間模組
import credentials  #載入credentials模組
from selenium.webdriver.chrome.options import Options   #載入瀏覽器options選項設定模組

options = Options()   #建立瀏覽器物件
options.add_argument("--disable-notifications")  #加入關閉通知的參數

driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)  #由chrome驅動程式管理員幫我們打開chrome瀏覽器，install()之後增加關閉通知的選項設定

driver.get("https://www.facebook.com/")   #瀏覽器進入facebook

email = driver.find_element(By.ID,"email")      #定位id輸入email的位置
password = driver.find_element(By.ID, "pass")   #定位id輸入password的位置

email.send_keys(credentials.email)             #利用send_keys輸入email        
password.send_keys(credentials.password)       #利用send_keys輸入password
password.submit()                              #利用submit發送

time.sleep(5)                                 #等待5秒

driver.get("https://www.facebook.com/ETtodayMOVIE")

for i in range(20):   #滾動捲軸20次
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)     #每次等待3秒
