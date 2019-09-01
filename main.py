print("enter username")
username=input()
print("enter password")
password=input()
print("enter the url")
url=input()

from func import *

path()
time.sleep(1)

url_name(url)

login(username,password)

first_picture()
like_pic()

continue_liking()