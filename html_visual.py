from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome import service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

choice = input("do you want to use Firefox or Chrome(F ; C) : ")

while True :
    if choice == "F":
        file = input("file: ")
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        break

    elif choice == "C" :
        file = input("file: ")
        service = service.Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        break

    input("press F or C : ")


driver.get("file://"+file)

f_time = os.stat(file)

while True :
    l_time = os.stat(file)
    if f_time != l_time :
        f_time = l_time
        driver.refresh()
    time.sleep(1)
