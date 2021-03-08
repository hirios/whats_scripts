from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import platform
import pyqrcode
import os


DEFAULT_USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'


options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--user-agent=' + DEFAULT_USER_AGENT)
options.add_argument('--headless')
options.add_argument('--window-size=1920x1080')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')


chromedriver = 'chromedriver.exe'


def half_char(u, d):
    half_matrix = {
        ('0', '0'):'\U00002588',
        ('1', '1'):' ',
        ('1', '0'):'\U00002584',
        ('0', '1'):'\U00002580'
    }
    return half_matrix[(u,d)]


def qr_half(txt):
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
    
  
driver = webdriver.Chrome(chromedriver, options=options)
os.system('cls')

print('→ ' + bcolors.OKGREEN + 'INFO: ' + bcolors.END + 'Browser inicializado')
driver.get('https://web.whatsapp.com/')
print('→ ' + bcolors.OKGREEN + 'INFO: ' + bcolors.END + 'Whatsapp Web Page OK\n')
sleep(4)

stop = 0
b = ""
while stop == 0:
    try:
        # VERIFICANDO O QR CODE SE ESTE ESTIVR VISÍVEL
        a = driver.find_element_by_xpath('//div[@class="_3jid7"]').get_attribute('data-ref')
        if a != b:
            QR(a)
            b = a
            sleep(0.5)
    except:
        try:
            # SE O QR CODE NÃO ESTIVER VISÍVEL, CLICAR PARA RECARREGAR
            driver.find_element_by_xpath('//div[@class="_3jid7 _267ZZ"]').click()
            sleep(1)
        except:
            stop = 1
            
print('→ ' + bcolors.OKGREEN + 'INFO: ' + bcolors.END + 'Logando...')



stop2 = 0
while stop2 == 0:
    try:
        driver.find_element_by_xpath('//span[@data-testid="menu"]')
        stop2 = 1
    except:
        sleep(0.5)
print('→ ' + bcolors.OKGREEN + 'INFO: ' + bcolors.END + 'Logado')
