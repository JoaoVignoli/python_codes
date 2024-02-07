from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
equipamentos = [
    '10.255.103.139'
]
for equipamento_ip in equipamentos:

    Url = f'http://{equipamento_ip}'
navegador.get(Url)
navegador.find_element('xpath', '//*[@id="Frm_Username"]').send_keys("admin")
navegador.find_element('xpath','//*[@id="Frm_Password"]').send_keys("admin")
navegador.find_element('xpath', '//*[@id="LoginId"]').click()