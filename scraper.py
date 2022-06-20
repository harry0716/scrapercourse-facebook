from selenium import webdriver  #載入瀏覽器驅動模組
from webdriver_manager.chrome import ChromeDriverManager  #載入瀏覽器驅動模組管理員，匯入chrome驅動程式管理員
from selenium.webdriver.common.by import By       #載入定位模組
import time   #載入時間模組
import credentials  #載入credentials模組

driver = webdriver.Chrome(ChromeDriverManager().install())    #由chrome驅動程式管理員幫我們打開chrome瀏覽器

driver.get("https://www.facebook.com/")   #瀏覽器進入facebook

email = driver.find_element(By.ID,"email")      #定位id輸入email的位置
password = driver.find_element(By.ID, "pass")   #定位id輸入password的位置

email.send_keys(credentials.email)             #利用send_keys輸入email        
password.send_keys(credentials.password)       #利用send_keys輸入password
password.submit()                              #利用submit發送

time.sleep(60)                                 #等待60秒
