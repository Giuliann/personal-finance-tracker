import uuid
from Controle_gastos.Backend.Token import remover_token

# Cria um token:
def new_token():
    return str(uuid.uuid4())

# Verifica a existencia do token:
def verify_token(token):
    return token is not None

# Fecha a sessão:
def logout():
    remover_token()