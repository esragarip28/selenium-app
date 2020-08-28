from selenium import webdriver
import time
import random

driver=webdriver.Chrome()
url="https://eksisozluk.com/yar-ve-yardimci-olmak--2262526?a=popular&p="
number=1
entries=[]
count=1
while number<=5:
    pageNumber=random.randint(1,6)
    newurl=url+str(pageNumber)
    driver.get(newurl)
    elements=driver.find_elements_by_css_selector(".content")
    for element in elements:
        entries.append(element.text)
        print(element.text)
    time.sleep(5)        
    number=number+1
    
with open("data.txt","w", encoding="utf-8") as file:
    for entry in entries:
        file.write(str(count)+".\n"+" : "+entry+"\n")
        count=count+1
driver.close()    
    
    

