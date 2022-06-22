from selenium import webdriver  #載入瀏覽器驅動模組
from webdriver_manager.chrome import ChromeDriverManager  #載入瀏覽器驅動模組管理員，匯入chrome驅動程式管理員
from selenium.webdriver.common.by import By       #載入定位模組
import time   #載入時間模組
import credentials  #載入credentials模組
from selenium.webdriver.chrome.options import Options   #載入瀏覽器options選項設定模組
from bs4 import BeautifulSoup 


options = Options()   #建立瀏覽器物件
options.add_argument("--disable-notifications")  #加入關閉通知的參數

driver = webdriver.Chrome(
    ChromeDriverManager().install(),chrome_options=options)  #由chrome驅動程式管理員幫我們打開chrome瀏覽器，install()之後增加關閉通知的選項設定
   
driver.get("https://www.facebook.com/")   #瀏覽器進入facebook

email = driver.find_element(By.ID,"email")      #定位id輸入email的位置
password = driver.find_element(By.ID, "pass")   #定位id輸入password的位置

email.send_keys(credentials.email)             #利用send_keys輸入email        
password.send_keys(credentials.password)       #利用send_keys輸入password
password.submit()                              #利用submit發送

time.sleep(10)                                 #等待10秒

driver.get("https://www.facebook.com/groups/235385084142732")  #netflix新台灣討論區(非官方)

for i in range(20):   #滾動捲軸20次
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(2)     #每次等待3秒

soup = BeautifulSoup(driver.page_source, "lxml")  #前面滾動捲軸後，就可以將網頁原始碼的內容傳入BS4

posts = soup.find_all("div",{"class":"du4w35lb l9j0dhe7"})

result = []
for post in posts:
    content = post.find("span",{"class":"d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d3f4x2em iv3no6db jq4qci2q a3bd9o3v b1v8xokw oo9gr5id hzawbc8m"})
    result.append(content.getText())
print(result)