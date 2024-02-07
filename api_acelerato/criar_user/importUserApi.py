import json
import os
import pandas as pd
import requests
from requests.auth import HTTPBasicAuth

# DADOS DE ACESSO A API;
url = f"https://atendimento.unifique.com.br/api/publica/usuarios"
usuario = ""
senha = ""

# DIRETÓRIO ATUAL DOS ARQUIVOS JSON E CSV
dir = os.path.dirname(os.path.abspath(__file__))
dirJsonNewUser = os.path.join(dir, "newuser.json")
dirCSV = os.path.join(dir, "newUser.csv")

# ABRE ARQUIVO CSV
dadosUsersCsv = pd.read_csv(dirCSV, delimiter=";",encoding="utf-8",usecols=["nome","email"])

# LE ARQUIVO JASON
with open(dirJsonNewUser, "r") as file:
    dados_json = json.load(file)

# LOOP PELAS LINHAS DO CSV ARMAZENA EM UM DICIONÁRIO;
for linha in dadosUsersCsv.values:
    user = dict(
        nome = linha[0],
        email = linha[1]
    )
# PREENCHE O CSV COM OS DADOS DO CSV EM SEU RESPECTIVO CAMPO;
    dados_json["email"] = user.get("email")
    dados_json["nome"] = user.get("nome")
    with open(dirJsonNewUser, "w") as arquivo:
        json.dump(dados_json,arquivo)
    response = requests.post(url, json=dados_json, auth=HTTPBasicAuth(usuario,senha), verify=False)
    if response.status_code == 201:
        print("Arquivo enviado")
    else:
        print("Falha ao enviar o arquivo JSON. Código de status:", response.status_code)
        print("Conteúdo da resposta:", response.text)
    print(dados_json)
