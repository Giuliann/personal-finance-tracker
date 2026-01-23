from datetime import date
import os

# Tempo de pesquisa maximo: 
def futuro():
    ano_futuro = date.today().year + 2
    return ano_futuro

# Tempo de pesquisa minima:
def passado():
    ano_passado = date.today().year - 20
    return ano_passado


# Consulta de meses: 
def meses():
    meses = { 1: 'Janeiro', 
          2: 'Fevereiro',
          3: 'Março',
          4: 'Abril',
          5: 'Maio',
          6: 'Junho',
          7: 'Julho',
          8: 'Agosto',
          9: 'Setembro',
         10: 'Outubro',
         11: 'Novembro',
         12: 'Dezembro'}
    return meses

def limpar():
    os.system('cls')