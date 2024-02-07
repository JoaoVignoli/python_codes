from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from netaddr import *
import time
import socket

class testar_porta:
    def __init__(self):
        resultadoTest = False
    
    def testar(self, host, port):
        timeout_seconds=1
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout_seconds)
        result = sock.connect_ex((host,int(port)))
        if result == 0:
            resultadoTest = True
            return resultadoTest
        else:
            resultadoTest = False
            return resultadoTest
        sock.close()

NAV_MAP = {
    "zte" : {
        'login' : '//*[@id="Frm_Username"]',
        'senha' : '//*[@id="Frm_Password"]',
        'loginBtn': '//*[@id="LoginId"]',
        'iframe': '//*[@id="mainFrame"]',
        'administration' : '//*[@id="Fnt_mmManager"]',
        'userMgnt' : '//*[@id="smUserMgr"]',
        'oldPass' : '//*[@id="Frm_OldPassword"]',
        'newPass' : '//*[@id="Frm_Password"]',
        'confirPass' : '//*[@id="Frm_CfmPassword"]',
        'passBtn' : '//*[@id="Btn_Submit"]',
        
    }
}


for i in range(1,254):
    ipAddress = f'10.255.103.{i}'
    print(ipAddress)
    testPorta = testar_porta()
    checkPort = testPorta.testar(ipAddress, 80)
    if checkPort:
        urlNav = f"http://{ipAddress}"
        servico = Service(ChromeDriverManager().install())
        navegador = webdriver.Chrome(service=servico)
        navegador.maximize_window()
        navegador.set_page_load_timeout(5)
        navegador.implicitly_wait(2);
        try:
            navegador.get(urlNav)
            time.sleep(1)
            navegador.refresh()
            time.sleep(1)
            try:
                navegador.find_element('xpath',NAV_MAP["zte"]["login"]).send_keys('admin')
                navegador.find_element('xpath',NAV_MAP["zte"]["senha"]).send_keys('admin')
                navegador.find_element('xpath',NAV_MAP["zte"]["loginBtn"]).click()
                navegador.switch_to.frame(navegador.find_element('xpath', NAV_MAP["zte"]["iframe"]))
                navegador.find_element('xpath',NAV_MAP["zte"]["administration"]).click()
                navegador.find_element('xpath',NAV_MAP["zte"]["userMgnt"]).click()
                navegador.find_element('xpath',NAV_MAP["zte"]["oldPass"]).send_keys('admin')
                navegador.find_element('xpath',NAV_MAP["zte"]["newPass"]).send_keys('8DAa84m7xG2zdid')
                navegador.find_element('xpath',NAV_MAP["zte"]["confirPass"]).send_keys('8DAa84m7xG2zdid')
                time.sleep(1)
                navegador.find_element('xpath',NAV_MAP["zte"]["passBtn"]).click()
                time.sleep(2)
                print('Senha Alterada!')
                navegador.quit()
            except:
                print('Senha Incorreta')
                navegador.quit()
        except:
            print('Sem acesso na ZTE')
            navegador.quit()
    else:
        print('Sem acesso na ZTE')