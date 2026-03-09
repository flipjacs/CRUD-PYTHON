import requests
import mysql.connector
from database import db_config
import re

cep = input("Digite um CEP: ")

if not re.fullmatch(r"\d{5}-?\d{3}", cep):
    print("FORMATO DE CEP INVÁLIDO!")

else:

    cep = cep.replace("-", "")
    url = f'https://viacep.com.br/ws/{cep}/json/'

    resposta = requests.get(url)
    dados = resposta.json()

    cursor = db_config.cursor()

    if "erro" in dados:
        print("CEP INVÁLIDO!")

    else:
        comando = '''
        INSERT INTO tb_endereco
        (cep, logradouro, bairro, cidade, estado)
        VALUES (%s,%s,%s,%s,%s)
        '''

        valores = (
            dados["cep"],
            dados["logradouro"],
            dados["bairro"],
            dados["localidade"],
            dados["uf"]
        )

        cursor.execute(comando, valores)
        db_config.commit()

        print("Endereço salvo no banco com sucesso!")
        print(valores)