from selenium import webdriver
from time import sleep

driver1 = webdriver.Chrome(executable_path="E:\Programs\YouTube\Viewbot\chromedriver_win32\chromedriver.exe")

driver1.get("Enter the link of the video")

while True:
    sleep(2)
    driver1.refresh()
    
