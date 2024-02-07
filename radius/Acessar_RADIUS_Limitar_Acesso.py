from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import time
import csv

def ler_usuarios_do_csv(nome_arquivo):
    usuarios = [] 
    with open(nome_arquivo, newline='', encoding='utf-8-sig') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        for linha in leitor:
            linha_sem_bom = {chave.replace('\ufeff', ''): valor for chave, valor in linha.items()}
            if 'Username' in linha_sem_bom and linha_sem_bom['Username'].strip():
                usuarios.append(linha_sem_bom['Username'])              
                print(f"Usuário adicionado: {linha_sem_bom['Username']}")
    return usuarios



nome_arquivo_csv = r'C:\Users\joao.vignoli\Desktop\USER_DISABLE.csv'

NAV_MAP = {
    "KACE" : {
        'Login' : '//*[@id="button_saml"]',
        'User' : '//*[@id="i0116"]',
        'Avancar' : '//*[@id="idSIButton9"]',
        'Senha' : '//*[@id="i0118"]',
        'Entrar' : '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div/input',
        'Sim' : '/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input',
        'Config' : '/html/body/nav/div/div[2]/section/ul/li[10]/header/a',
        'Usuarios' : '/html/body/nav/div/div[2]/section/ul/li[10]/div/ul/li[2]/a',
        'Pesquisa' : '/html/body/div[2]/div[2]/div[2]/div/form/input[1]',
        'Erro' : '/html/body/div[2]/section/section[3]/form/div/div[1]/div[2]/table/tbody/tr/td',
     }
}

usuarios = ler_usuarios_do_csv(nome_arquivo_csv)

urlNav = f"https://kace.redeunifique.com.br/admin"
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.maximize_window()
navegador.set_page_load_timeout(30)
navegador.implicitly_wait(24)
navegador.get(urlNav)
time.sleep(1)
navegador.find_element('xpath',NAV_MAP["KACE"]["User"]).send_keys('joao.vignoli@redeunifique.com.br')
navegador.find_element('xpath',NAV_MAP["KACE"]["Avancar"]).click()
navegador.find_element('xpath',NAV_MAP["KACE"]["Senha"]).send_keys('@69xjnOeJ69@')
navegador.find_element('xpath',NAV_MAP["KACE"]["Entrar"]).click()
time.sleep(1)
navegador.find_element('xpath',NAV_MAP["KACE"]["Sim"]).click()
navegador.find_element('xpath',NAV_MAP["KACE"]["Config"]).click()
navegador.find_element('xpath',NAV_MAP["KACE"]["Usuarios"]).click()

for usuario in usuarios:
    navegador.find_element('xpath',NAV_MAP["KACE"]["Pesquisa"]).send_keys(usuario)
    #não encontrou o campo pesquisa
    try:        
        print(f"Alteração realizada para o usuário: {usuario}")
    except NoSuchElementException:
        print(f"Campo senha não encontrado para: {usuario}")

navegador.quit()