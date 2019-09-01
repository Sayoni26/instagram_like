from selenium import webdriver
import time

# enter the path where the chromedriver.exe file exists in your system
def path():  
    global chrome
    print("enter the driver path")
    exe_path=input()
    chrome=webdriver.Chrome(executable_path=exe_path)

# enter the url of the page     
def url_name(url):  
    chrome.get(url)  # the web page opens up
    time.sleep(4)   # webdriver will wait for 4 sec before throwing a NoSuchElement exception

# enter your login information
def login(username,your_password):
     
    log_but=chrome.find_element_by_xpath('//button[text()="Log In"]')  # finds the login button
    time.sleep(2)
    log_but.click()  # clicks the login button
    time.sleep(4)
    usern=chrome.find_element_by_name("username")  # finds the username box
    usern.send_keys(username)   # sends the entered username
    passw=chrome.find_element_by_name("password")  #finds the password box
    passw.send_keys(your_password)  # sends the entered password
    log_cl=chrome.find_element_by_class_name("L3NKy")   # finds the login button
    log_cl.click()   # clicks the login button
    #chrome.implicitly_wait(6)
    time.sleep(4)

# opens the first picture 
def first_picture():
    pic=chrome.find_element_by_class_name("_9AhH0")  # finds the first picture 
    pic.click()  # clicks on the first picture

#likes a picture
def like_pic():
    time.sleep(4)
    like=chrome.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button/span')
    time.sleep(2)
    like.click()

# clicks on the next button
def next_picture():
    time.sleep(2)
    nex=chrome.find_element_by_class_name("HBoOv")  # finds the button which gives the next picture
    time.sleep(1)
    return nex

# cotinues liking pictures till it is not able to find the next button
def continue_liking():
    while(True):
        next_el=next_picture()
        if next_el!=False:  # if next button is there then
            next_el.click()  # click the next button
            time.sleep(2)
            like_pic()  # like the picture
            time.sleep(2)            
        else:
            print("not found")   # if no next button then print not found and exit
            break










