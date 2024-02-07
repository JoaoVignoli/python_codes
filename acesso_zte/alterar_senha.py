from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Configurações do dispositivo
ip = '192.168.1.1'  # Endereço IP do equipamento ZTE F660
username = 'admin'  # Nome de usuário para fazer login
password = 'admin'  # Senha atual
new_password = 'nova_senha'  # Nova senha a ser definida

# Configurações do navegador
driver_path = 'C:/path/to/chromedriver.exe'  # Caminho para o executável do ChromeDriver

# Inicializa o navegador Chrome
driver = webdriver.Chrome(executable_path=driver_path)

# Acessa a página de login do equipamento
driver.get(f'http://{ip}/')

# Insere as credenciais de login
username_input = driver.find_element_by_id('username')
username_input.send_keys(username)

password_input = driver.find_element_by_id('password')
password_input.send_keys(password)

# Efetua o login
password_input.send_keys(Keys.RETURN)

# Navega para a página de alteração de senha
driver.get(f'http://{ip}/password')

# Insere a nova senha
new_password_input = driver.find_element_by_id('new_password')
new_password_input.send_keys(new_password)

confirm_password_input = driver.find_element_by_id('confirm_password')
confirm_password_input.send_keys(new_password)

# Envia o formulário de alteração de senha
confirm_password_input.send_keys(Keys.RETURN)

# Fecha o navegador
driver.quit()
