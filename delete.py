from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time
import sys


options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
CHROMEDRIVER = ChromeDriverManager().install()


def stime(seconds):
    return time.sleep(seconds)


def scroll_to_end(DRIVER, USER):
    browser = DRIVER
    browser.get("https://www.instagram.com/" + USER)

    stime(5)
    stop = False
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    meta = int(browser.find_element_by_xpath("//li/span/span").text)

    links_photos = []
    while(stop==False):
        links = [x.get_attribute("href") for x in browser.find_elements_by_xpath('//div[@style]//div//div//a[@tabindex="0"]')]
        [links_photos.append(x) for x in links if not x in links_photos]
        if not len(links_photos) == meta:
            lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            stime(3)
        else:
            stop = True            

            
    return links_photos


def login_to_site():
    try:
        print()
        print ('!!! O SISTEMA IRÁ DELETAR TODOS POST DO SEU INSTAGRAM !!!')

        user_agent = "Mozilla/5.0 (Android 9; Mobile; rv:68.0) Gecko/68.0 Firefox/68.0"
        browser = webdriver.Chrome(CHROMEDRIVER, options=options)
        browser.set_window_size(360,640)
        browser.get("https://www.instagram.com/accounts/login/")
        stime(2)

        insta_username = "eulinadoliveira"
        insta_password = "fendadobiquini"

        eUser = browser.find_elements_by_xpath(
            "//input[@name='username']")
        ActionChains(browser).move_to_element(eUser[0]). \
            click().send_keys(insta_username).perform()
        stime(1)
        ePass = browser.find_elements_by_xpath(
            "//input[@name='password']")
        stime(1)
        ActionChains(browser).move_to_element(ePass[0]). \
            click().send_keys(insta_password).perform()
        stime(1)
        login_button = browser.find_element_by_xpath(
            "//*[contains(text(), 'Log In')]")
                     
        ActionChains(browser).move_to_element(login_button).click().perform()
        stime(7)

        links_photos = scroll_to_end(browser, insta_username)
        deleted_urls = []
        
        try:
            print ('DELETANDO POSTS!')
            for link in links_photos:
                browser.get(link)
                stime(5)
                
                if ("Sorry, this page isn't available." in browser.page_source):
                    print("!! ESSE POST JÁ FOI DELETADO !!")
                else:                
                    options_button = browser.find_element_by_xpath(
                            "//div[@class='MEAGs']//*[@aria-label='More options']")
                    ActionChains(browser).move_to_element(options_button).click().perform()                
                    stime(2)
                    delete_button = browser.find_element_by_xpath(
                        "//button[text()='Delete']")
                    ActionChains(browser).move_to_element(delete_button).click().perform()
                    stime(2)
                    confirm_delete = browser.find_element_by_xpath(
                        "//button[text()='Delete']")
                    ActionChains(browser).move_to_element(confirm_delete).click().perform()
                    stime(2)
                    print ('POST DELETADO: ' + link)


            print ("POSTS EXCLUÍDOS COM SUCESSO")
            browser.close()

        except Exception as err:
            print (err)
            browser.close()
            sys.exit()
    
    except Exception as err:
        print (err)  

       
login_to_site()