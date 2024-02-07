from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import ping3

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
equipamentos = ['10.255.103.139', '10.255.103.140']

def check_online_status(hostname):
    response_time = ping3.ping(hostname)
    if response_time is not None:
        print(f"{hostname} equipamento acessado. Tempo de resposta: {response_time} ms")
        Url = f'http://{hostname}'
        navegador.get(Url)
        navegador.find_element('xpath', '//*[@id="Frm_Username"]').send_keys("admin")
        navegador.find_element('xpath', '//*[@id="Frm_Password"]').send_keys("admin")
        navegador.find_element('xpath', '//*[@id="LoginId"]').click()
        
    else:
        print(f"{hostname} está offline.")

# Verificar status de cada equipamento
for equipamento_ip in equipamentos:
    check_online_status(equipamento_ip)