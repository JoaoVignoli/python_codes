import pandas as pd
import os
import requests
from requests.auth import HTTPBasicAuth
import json


url_user = "https://homologunifique.acelerato.com/api/publica/usuarios"
url_emails = "https://homologunifique.acelerato.com/api/publica/usuarios/emails"
user = "joao.vignoli@redeunifique.com.br"
password = "LKxXELXfvAAixQapypvBqQ=="

dir = os.path.dirname(os.path.abspath(__file__))
path_csv = os.path.join(dir,"USER_AD_copy.csv")
path_json_desabilitar_user = os.path.join(dir,"desabilitar_user_acelerato.json")


users_ad = pd.read_csv(path_csv,delimiter=",",encoding="utf-8",usecols=["Name","UserPrincipalName","Enabled"])

def pesquisa_email_acelerato(email_ad):
    response = requests.get(url_emails, auth=HTTPBasicAuth(user,password))
    if response.status_code == 200:
        data = response.json()
        if email_ad in data:
            return True
        else:
            return False
    else:
        print(f"Código do erro: {response.status_code}")
        print(response.text)

def preenche_json_desabilitar_user(email, nome):
    with open(path_json_desabilitar_user, "r") as file:
        user = json.load(file)
    user["email"] = email
    user["nome"] = nome
    with open(path_json_desabilitar_user, "w") as arquivo:
        json.dump(user, arquivo)

def desabilita_user_acelerato():
    for item in users_ad.values:
        if item[2] == False:
            localizou_email = pesquisa_email_acelerato(item[1])
            if localizou_email == True:
                response = requests.get (url_user, params={"email": item[1]}, auth=HTTPBasicAuth(user,password))
                if response.status_code == 200:
                    data = response.json()
                    Nome = "nome"
                    ID = "usuarioKey"
                    Email = "email"
                    Status = "ativo"
                    for item in data:
                        if item[Status] == True:
                            usuarioKey = item[ID]
                            preenche_json_desabilitar_user(item[Email], item[Nome])
                            with open(path_json_desabilitar_user, "r") as file:
                                dados_user = json.load(file)
                            url_alterar_user = f"https://homologunifique.acelerato.com/api/publica/usuarios/{usuarioKey}"
                            response = requests.put(url_alterar_user, json=dados_user, auth=HTTPBasicAuth(user,password))
                            if response.status_code == 204:
                                print(f"ID: {item[ID]} {item[Nome]} desabilitado com sucesso")
                            else:
                                print(response.status_code)
                                print(response.text)
            else:
                print(f"Email: {item[1]} não localizado")


desabilita_user_acelerato()
