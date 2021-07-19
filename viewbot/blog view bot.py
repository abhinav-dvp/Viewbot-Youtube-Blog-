from selenium import webdriver
from time import sleep

driver1 = webdriver.Chrome(executable_path="C:/Users/Abhinav dont touch/Desktop/YouTube/chromedriver_win32/chromedriver.exe")

driver1.get("Enter the link of your blog")
a = 300
# a value is for 50 mb data consumption

while a > 0:
    sleep(1)
    driver1.refresh()
    a -=1
