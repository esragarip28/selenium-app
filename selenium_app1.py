from selenium import webdriver
import time
browser=webdriver.Chrome()
url="https://eksisozluk.com/yar-ve-yardimci-olmak--2262526?a=popular"

browser.get(url) #sanal browserla bu url acilacak burada bu url e git dedik
time.sleep(10)#acilan sayfanin ne kadar sure acik kalacagini belirlemek için yaptik.
element=[]
element=browser.find_elements_by_css_selector(".content")
for element in element:
    print(element.text)
browser.close()    
   
