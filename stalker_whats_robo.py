import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
# pyarmor==6.6.2
    

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = "C:\\"
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()
        
##from selenium.webdriver.chrome.options import Options
##from selenium.webdriver.common.keys import Keys
##from playsound import playsound
##from selenium import webdriver
##from time import sleep
##import os
##
##
##options = Options()
##options.add_argument("user-data-dir=./")
##driver = webdriver.Chrome(options=options)
##driver.get('https://web.whatsapp.com/')
##
##
##stop = 0
##while stop == 0:
##    try:
##        driver.find_element_by_xpath('//div[@contenteditable="true"]')
##        stop = 1
##    except:
##        pass
##
##    sleep(1)
##
### CLICA NO CAMPO DE PESQUISA, LIMPA, DEPOIS DIGITA
##def busca(nome):
##    driver.find_element_by_xpath('//div[@contenteditable="true"]').clear()
##    driver.find_element_by_xpath('//div[@contenteditable="true"]').send_keys(nome)
##    sleep(1.5)
##
##
##def clica(nome):
##    driver.find_element_by_xpath(f'//span[@title="{nome}"]').click()
##
##
##
##while True:
##    try:
##        busca('Wili')
##        clica('Wili')
##        driver.find_element_by_xpath('//span[@title="online"]')
##        os.system('cls')
##        
##        playsound('Desktop\erro.mp3')
##    except:
##        os.system('cls')
##        print('OFLINE')
##    
##    sleep(0.2)
