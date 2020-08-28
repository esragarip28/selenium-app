from selenium import webdriver
import time
import info

driver=webdriver.Chrome()
url="https://twitter.com/twitter "
driver.get(url)
time.sleep(5)
make_enter=driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/header/div[2]/div[1]/div/div[2]/div/div[1]/a/div")
make_enter.click()
time.sleep(5)
username=driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input")
password=driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input")
username.send_keys(info.username)
password.send_keys(info.password)
time.sleep(3)
login=driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/form/div/div[3]/div/div")
login.click()
time.sleep(3)
home=driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[1]")
home.click()

searchData=driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]")
searchData.click()
searchArea=driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div[2]/input")
searchArea.send_keys("#yazilimayolver")
time.sleep(5)
searchArea.submit()

#tüm tweetleri almak için scroll özelligini yapmak amacıyla biz javascript kodlarını kullanıyoruz...

lenOfPage =driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True
tweets=[]
number=1
while number<6:
    elements=driver.find_elements_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div/div/div/section/div/div/div/div[2]/div/div/article/div/div/div/div[2]/div[2]/div"+"["+str(number)+"]")
    number=number+1
for element in elements:
    print(element.text)
    tweets.append(element.text)
    
tweetCount=1
with open("tweets.txt ","w",encoding="UTF-8") as file:
    for tweet in tweets:
        file.write(str(tweetCount)+":\n "+ tweet+"\n")
        tweetCount=tweetCount+1

time.sleep(10)
driver.close()