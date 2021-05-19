from selenium import webdriver
from time import sleep


user = 'eulinadoliveira'
password = 'fendadobiquini'


class Insta():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.lista1 = []
        self.lista2 = []

        self.lista_final = []


    def login(self):
        self.driver.get('https://www.instagram.com/')
        sleep(3)
        self.driver.find_element_by_name('username').send_keys(user)
        self.driver.find_element_by_name('password').send_keys(password)
        ENTER = 'Igw0E.IwRSH.eGOV_._4EzTm'
        self.driver.find_element_by_class_name(ENTER).click()
        sleep(4)


    def set_profile(self, url):
        self.driver.get(url)
        sleep(3)


    def updateLists(self):
        self.lista1 = self.driver.find_elements_by_xpath('//div[@class="C4VMK"]/span')[1:]
        self.lista2 = self.driver.find_elements_by_xpath('//a[@class="sqdOP yWX7d     _8A5w5   ZIAjV "]')[2:]


    def parseLists(self, numero):
        if numero == 1:
            for x in range(0, len(self.lista2)):
                print("--> " + self.lista2[x].text + ": " + self.lista1[x].text)


    def carregar(self):
        try:
            self.driver.find_elements_by_xpath('//span[@class="glyphsSpriteCircle_add__outline__24__grey_9 u-__7"]')[0].click()
        except IndexError:
            sleep(2.5)
            try:
                self.driver.find_elements_by_xpath('//span[@class="glyphsSpriteCircle_add__outline__24__grey_9 u-__7"]')[0].click()
            except:
                print('Erro ao carregar comentários!!')
            

        
tay = Insta()
tay.login()
tay.set_profile('https://www.instagram.com/p/CLAcq9eL1yF/')
tay.updateLists()
tay.parseLists(1)


    
