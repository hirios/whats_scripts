from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import wikipedia
import platform
import pyqrcode
import os


DEFAULT_USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'


options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("user-data-dir=C:\\Users\\Novo\\AppData\\Local\\Google\\Chrome\\User Data\\bot_data")
options.add_argument('--user-agent=' + DEFAULT_USER_AGENT)
options.add_argument('--headless')
options.add_argument('--window-size=1920x1080')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')


CHROMEDRIVER = 'chromedriver.exe'


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
        self.select_user('Clareira filosófica')
        self.wait_messages()


    def start_driver(self):
        """ Instancia o webdriver (chromedriver) e logo em seguida entra na página do whatsapp """

        self.driver = webdriver.Chrome(CHROMEDRIVER, options=options)
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
                #print('QR EXISTE')
                a = self.driver.find_element_by_xpath('//div[@class="_3jid7"]').get_attribute('data-ref')
                if a != b:
                    QR(a)
                    b = a
                    #print('QR DIFERENTE')
                    sleep(0.5)
            except:
                try:
                    # SE O QR CODE NÃO ESTIVER VISÍVEL, CLICAR PARA RECARREGAR
                    #print('SUMIU')
                    self.driver.find_element_by_xpath('//div[@class="_3jid7 _267ZZ"]').click()
                    sleep(1)
                    #print('cliquei')
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


    def select_user(self, nome):
        self.driver.find_element_by_xpath(f'//span[@title="{nome}"]').click()


    def old_messages(self):
        msg = self.driver.find_elements_by_xpath('//span[@class="_3-8er selectable-text copyable-text"]')[-1].text
        time = self.driver.find_elements_by_xpath('//span[@class="_17Osw"]')[-1].text
        return (msg, time)


    def send_messages(self, message):
        campo_de_msg = self.driver.find_elements_by_xpath('//div[@class="_2_1wd copyable-text selectable-text" and @data-tab="6"]')[0]
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
                        except:
                            print(argumento, 'Não executado com sucesso!')
                        sleep(0.2)
                    else:
                        sleep(0.2)
                

                  
whats = Nagazap()
input()
##url = pyqrcode.create('http://uca.edu')
##print(url.terminal(quiet_zone=1))
