from calcula_bonus import calcula_bonus_kpi
import csv
import os
from datetime import datetime

continuar:bool = True

while continuar: 
    nome_valido: bool = False
    salario_valido: bool = False
    bonus_valido: bool = False

    while not nome_valido:
        try:
            nome:str = input("Digite seu nome: ")

            # Verifica se o nome está vazio
            if len(nome.replace(" ","")) == 0:
                raise ValueError("O nome não pode estar vazio.")
            # Verifica se há números no nome
            elif any(char.isdigit() for char in nome):
                raise ValueError("O nome não deve conter números.")
            else:
                nome_valido: bool = True
        except ValueError as e:
            print(e)

    # Solicita ao usuário que digite o valor do seu salário e converte para float
    while not salario_valido:
        try:
            salario: float = float(input("Digite o valor do seu salário: "))
            if salario < 0:
                print("Por favor, digite um valor positivo para o salário.")
            else:
                salario_valido: bool = True
        except ValueError:
            print("Entrada inválida para o salário. Por favor, digite um número.")

    # Solicita ao usuário que digite o valor do bônus recebido e converte para float
    while not bonus_valido:
        try:
            bonus: float = float(input("Digite o valor do bônus recebido: "))
            if bonus < 0:
                print("Por favor, digite um valor positivo para o bônus.")
            else:
                bonus_valido: bool = True
        except ValueError:
            print("Entrada inválida para o bônus. Por favor, digite um número.")

    #Calcula o bônus que será recebido e retorna os dados em uma lista [nome, salario, bonus, bonus recebido]
    resultado_bonus = calcula_bonus_kpi(nome,salario,bonus) 
    resultado_bonus["data_inserção"] = datetime.today().strftime("%D-%M-%Y %H:%M:%S")

    #Insere todos esses dados em um CSV para manter histórico
    caminho_arquivo:str = "bonus_por_pessoa.csv"
    campos = ["nome","salario","bonus_percetual","bonus_recebido","data_inserção"]

    with open(caminho_arquivo,mode="a",newline="",encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campos)

        if os.stat(caminho_arquivo).st_size == 0:
            escritor.writeheader()

        escritor.writerow(resultado_bonus)


    variacoes_sim:list = ["SIM","S","SI","Y","YES"]
    if input("Deseja inserir outro valor? [S/N]").upper() not in  variacoes_sim:
        continuar = False