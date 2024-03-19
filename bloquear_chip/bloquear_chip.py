from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pyautogui
import time
import os
import pandas as pd
import logging

dir = os.path.dirname(os.path.abspath(__file__))
dir_numeros = os.path.join(dir, "numeros.csv")
numeros = pd.read_csv(dir_numeros,encoding="utf-8")
logging.basicConfig(format="%(asctime)s:%(levelname)s:%(filename)s:%(message)s", filename="log_block_numbers.log", level=logging.INFO)
    
url = ""
user = ""
password = ""

NAV_MAP = {
    "CRM" : {
        'Botao_Validar' : '//*[@id="pt1:pt_sf1:pt_captcha"]',
        'User' : '//*[@id="pt1:pt_sf1:pt_it1::content"]',
        'Senha' : '//*[@id="pt1:pt_sf1:pt_it2::content"]',
        'Botao_Acessar' : '//*[@id="pt1:pt_sf1:pt_checkuser"]',
        'Criar_Pedido' : '//*[@id="pt1:pt_sfm1j_id_4:pt_cl4"]',
        'Pesquisa_Numero' : '//*[@id="pt1:r1:0:pt_s1:it2::content"]',
        'Botao_Pesquisar' : '//*[@id="pt1:r1:0:pt_s1:cb1"]/span',
        'Botao_Nao' : '//*[@id="pt1:r1:1:cb2"]',
        'Tipo_Conta' : '//*[@id="pt1:r1:2:pt1:soc1::content"]',
        'Tipo' : '//*[@id="pt1:r1:2:pt1:soc2::content"]',
        'Categoria' : '//*[@id="pt1:r1:2:pt1:soc3::content"]',
        'Subcategoria' : '//*[@id="pt1:r1:2:pt1:soc4::content"]',
        'Selecionar' : '//*[@id="pt1:r1:2:pt1:cb1"]',
        'ID' : '//*[@id="pt1:r1:3:pt1:pt2222:soc1::content"]',
        'Proximo' : '//*[@id="pt1:r1:3:pt1:pt2222:cb1"]',
        '30_Dias' : '//*[@id="pt1:r1:4:pt1:pt2222:sor1:_1"]',
        'Proximo2' : '//*[@id="pt1:r1:4:pt1:pt2222:ctb1"]',
        'Executar_Ordem' : '//*[@id="pt1:r1:5:pt1:pt2222:cb10"]',
        'OK' : '//*[@id="pt1:r1:5:pt1:pt2222:popupError:dc_d1::ok"]',
        'Deslogar' : '//*[@id="pt1:r1:5:pt1:pt_cb2"]/img'
     }
}

screen_width, screen_height = pyautogui.size()

# Defina as coordenadas da posição para onde deseja mover o cursor
x_position = 969
y_position = 288

service = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=service)
logging.info("Inicio da execucao")
navegador.maximize_window()
navegador.set_page_load_timeout(30)
navegador.implicitly_wait(24)
navegador.get(url=url)
time.sleep(25)
navegador.find_element('xpath',NAV_MAP["CRM"]["User"]).send_keys(user)
navegador.find_element('xpath',NAV_MAP['CRM']["Senha"]).send_keys(password)
time.sleep(5)
navegador.find_element('xpath',NAV_MAP['CRM']["Botao_Validar"]).click()
time.sleep(15)
navegador.find_element('xpath',NAV_MAP['CRM']["Botao_Acessar"]).click()
time.sleep(15)

for numero in numeros.values:
    str_numero =' '.join(map(str, numero))
    pyautogui.moveTo(x_position, y_position)
    pyautogui.moveTo(984, 411)
    pyautogui.click(235,390)
    time.sleep(15)
    navegador.find_element('xpath',NAV_MAP['CRM']["Pesquisa_Numero"]).send_keys(str_numero)
    time.sleep(2)
    navegador.find_element('xpath',NAV_MAP['CRM']["Botao_Pesquisar"]).click()
    navegador.find_element('xpath',NAV_MAP['CRM']["Botao_Nao"]).click()
    time.sleep(5)
    navegador.find_element('xpath',NAV_MAP['CRM']["Tipo_Conta"]).click()
    time.sleep(2)
    pyautogui.click(378,763)
    time.sleep(2)
    navegador.find_element('xpath',NAV_MAP['CRM']["Tipo"]).click()
    time.sleep(2)
    pyautogui.click(378,809)
    time.sleep(2)
    navegador.find_element('xpath',NAV_MAP['CRM']["Categoria"]).click()
    time.sleep(2)
    pyautogui.click(378,842)
    time.sleep(2)
    navegador.find_element('xpath',NAV_MAP['CRM']["Subcategoria"]).click()
    time.sleep(2)
    pyautogui.click(378,870)
    time.sleep(5)
    pyautogui.click(378,908)
    time.sleep(5)
    navegador.find_element('xpath',NAV_MAP['CRM']["Selecionar"]).click()
    time.sleep(2)
    navegador.find_element('xpath',NAV_MAP['CRM']["ID"]).click()
    time.sleep(2)
    pyautogui.click(326,863)
    time.sleep(2)
    navegador.find_element('xpath',NAV_MAP['CRM']["Proximo"]).click()
    time.sleep(2)
    navegador.find_element('xpath',NAV_MAP['CRM']["30_Dias"]).click()
    time.sleep(5)
    navegador.find_element('xpath',NAV_MAP['CRM']["Proximo2"]).click()
    time.sleep(5)
    navegador.find_element('xpath',NAV_MAP['CRM']["Executar_Ordem"]).click()
    time.sleep(10)
    navegador.find_element('xpath',NAV_MAP['CRM']["OK"]).click()
    time.sleep(5)
    navegador.find_element('xpath',NAV_MAP['CRM']["Deslogar"]).click()
    time.sleep(15)
    navegador.execute_script("window.scrollTo(0, 0);")
    time.sleep(5)
    logging.info(f"Numero: {str_numero} bloqueado")
logging.info(f"Fim da execucao")