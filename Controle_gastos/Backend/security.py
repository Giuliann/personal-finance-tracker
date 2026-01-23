import bcrypt

# Cria uma Hash para senha:
def hash_senha(senha: str):
    return bcrypt.hashpw(
        senha.encode(),
        bcrypt.gensalt()
    ).decode()

# Verifica o hash:
def verify_senha(senha: str, hash: str):
    return bcrypt.checkpw(
        senha.encode(),
        hash.encode()
    )