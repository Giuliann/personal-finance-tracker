import json
import os

arq_token = 'token.json'

def salvar_token(token):
    with open(arq_token, 'w') as f:
        json.dump({'token': token}, f)

def carregar_token():
    if not os.path.exists(arq_token):
        return None

    with open(arq_token, 'w') as f:
        return json.load(f).get('token')
    
def remover_token():
    if not os.path.exists(arq_token):
        os.remove(arq_token)
