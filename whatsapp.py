from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import wikipedia
import platform
import pyqrcode
import os


DEFAULT_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43'


options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
#options.add_argument("user-data-dir=C:\\Users\\Novo\\AppData\\Local\\Google\\Chrome\\User Data\\bot_data")
options.add_argument('--user-agent=' + DEFAULT_USER_AGENT)
options.add_argument('--headless')
options.add_argument('--window-size=1920x1080')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')


CHROMEDRIVER = ChromeDriverManager().install()


def half_char(u, d):
    half_matrix = {
        ('0', '0'):'\U00002588',
        ('1', '1'):' ',
        ('1', '0'):'\U00002584',
        ('0', '1'):'\U00002580'
    }
    return half_matrix[(u,d)]


def qr_half(txt, printt=False):
    a = txt.split('\n')
    i = 0
    r = ''
    while i < len(a):
        l1 = a[i]
        i += 1
        l2 = a[i]
        if (l2 < l1):
            l2 += '1'*len(l1)
        i += 1
        r += ''.join(map(half_char,list(l1),list(l2)))+'\n'

    print(r)
    

def QR(text):
    url = pyqrcode.create(text)
    qr_half(url.text())


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    


class Nagazap():
    def __init__(self):
        wikipedia.set_lang("pt")
        self.antiga = None
        self.start_driver()
        self.wait_scan()
        self.wait_login()
        self.search_user("Clareira Filosofica")
        self.wait_messages()


    def start_driver(self):
        """ Instancia o webdriver (chromedriver) e logo em seguida entra na página do whatsapp """

        self.driver = webdriver.Chrome("chromedriver.exe", options=options)
        os.system('cls')

        print('→ ' + bcolors.OKGREEN + 'INFO: ' + bcolors.END + 'Browser inicializado')
        self.driver.get('https://web.whatsapp.com/')
        print('→ ' + bcolors.OKGREEN + 'INFO: ' + bcolors.END + 'Whatsapp Web Page OK\n')
        sleep(4)


    def wait_scan(self):
        """ Aguarda o QRCODE ser escaneado """

        stop = 0
        b = ""

        while stop == 0:
            try:
                # VERIFICANDO O QR CODE SE ESTE ESTIVR VISÍVEL
                a = self.driver.find_element_by_xpath('//div[@data-ref]').get_attribute('data-ref')
                if a != b:
                    QR(a)
                    b = a
                    #print('QR DIFERENTE')
                    sleep(0.5)
            except:
                try:
                    # SE O QR CODE NÃO ESTIVER VISÍVEL, CLICAR PARA RECARREGAR
                    self.driver.find_element_by_xpath('//div/span/button').click()
                    sleep(1)
                except:
                    stop = 1

        print('→ ' + bcolors.OKGREEN + 'INFO: ' + bcolors.END + 'Logando...')
        

    def wait_login(self):
        """ Aguarda o login estar completo """

        stop2 = 0
        while stop2 == 0:
            try:
                self.driver.find_element_by_xpath('//span[@data-testid="menu"]')
                stop2 = 1
            except:
                sleep(0.5)

        print('→ ' + bcolors.OKGREEN + 'INFO: ' + bcolors.END + 'Logado')


    def search_user(self, nome):
        first = self.driver.find_element_by_xpath('//div[@contenteditable="true"]')
        first.clear()
        first.send_keys(nome)
        first.send_keys(Keys.ENTER)
        sleep(1.5)


    def old_messages(self):
        msg = [x.text for x in self.driver.find_elements_by_xpath('//div[@data-pre-plain-text]/div/span')][-2]
        time = [x.text for x in self.driver.find_elements_by_xpath('//div[@data-testid="msg-meta"]/span')][-2]
        return (msg, time)


    def send_messages(self, message):
        campo_de_msg = self.driver.find_element_by_xpath('//div[@role="textbox" and @spellcheck="true"]')
        campo_de_msg.click()
        campo_de_msg.clear()
        campo_de_msg.send_keys(message)
        campo_de_msg.send_keys(Keys.ENTER)


    def wait_messages(self):
        while True:
            if not self.antiga:
                self.antiga = self.old_messages()
                sleep(0.2)
            else:
                new = self.old_messages()                
                if self.antiga != new:
                    self.antiga = new
                    
                    argumento = new[0].split()[0].lower()
                    query = ' '.join(new[0].split()[1:])    
                            
                    if argumento == '!wiki':
                        try:
                            sumary = wikipedia.summary(query)
                            self.send_messages(sumary)
                        except Exception as e:
                            print(argumento, 'Não executado com sucesso!')
                            print(e)
                        sleep(0.2)
                    else:
                        sleep(0.2)
                

    def verify_user(self):
        stop = 1
        while stop == 1:
            try:
                self.driver.find_element_by_xpath('//header/div[2]/div/div/span').text
                print('ESSE USUÁRIO EXISTE')
                stop = 0
            except:
                try:
                    self.driver.find_element_by_xpath('//div[@data-animate-modal-popup="true"]')
                    text = self.driver.find_element_by_xpath('//div[@data-animate-modal-popup="true"]/div').text
                    if text == 'O número de telefone compartilhado através de url é inválido.\nOK':
                        print("USUÁRIO NAO EXISTE")
                        stop = 0
                except:
                    pass                

                  
whats = Nagazap()
input()
##url = pyqrcode.create('http://uca.edu')
##print(url.terminal(quiet_zone=1))



