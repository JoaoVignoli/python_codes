from msal import ConfidentialClientApplication
import requests

# Configurações de autenticação OAuth 2.0
client_id = ''
client_secret = ''
tenant_id = ''

authority = f'https://login.microsoftonline.com/{tenant_id}'

msal_scope = ['https://graph.microsoft.com/.default']

onedrive_folder_id = '4a7f0f05-0dc6-4707-9548-a44b976fea97'
csv_file_path = 'userAtivos.txt'

msal_app = ConfidentialClientApplication(
    client_id=client_id,
    client_credential=client_secret,
    authority=authority
)

result = msal_app.acquire_token_silent(
    scopes=msal_scope,
    account=None
)

if not result:
    result = msal_app.acquire_token_for_client(scopes=msal_scope)

if "access_token" in result:
    access_token = result["access_token"]
else:
    raise Exception("No access token found")

url=f'https://graph.microsoft.com/v1.0/drive/items/{onedrive_folder_id}:/{csv_file_path}:/content'
#print(access_token)

with open(csv_file_path, 'rb') as csv_file:
        headers = {
            'Authorization': 'Bearer ' + access_token,
            'Content-Type': 'application/octet-stream',
            'Content-Disposition': f'attachment; filename="{csv_file_path}"'
        }
        upload_response = requests.post(url, data=csv_file, headers=headers)

# Verifique se o upload foi bem-sucedido
if upload_response.status_code == 200:
        print('Arquivo CSV enviado com sucesso para o Excel Online!')
else:
        print(f'Falha ao enviar o arquivo CSV. Código de status: {upload_response.status_code}')
        print(upload_response.text)
        print(f'Status Code: {upload_response.status_code}')
        print('Request Headers:')
        print(upload_response.request.headers)
        print('Request Body:')
        print(upload_response.request.body)
        print('Response Headers:')
        print(upload_response.headers)
        print('Response Body:')
        print(upload_response.text)
