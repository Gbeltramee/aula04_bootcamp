# nome = input("Nome:")
# Media = int(input(f"Média de {nome}:"))
# if Media > 7:
#   situacao = "Aprovado"
# else:
#   situacao = "Reprovado"

# dicionario = {
#   "Nome:":nome,
#   "Media":Media,
#   "Situação":situacao
#   }

# print(dicionario)


# import random

# jogadores = {}

# for numero in range(1,5):
#   nomejogador = "jogador"+str(numero)

#   jogadores[nomejogador] = {
#     "nome":nomejogador,
#     "pontuação":random.randint(1,6)
#   }

# jogadores_ordenados = sorted(jogadores.items(), key=lambda item: item[1]["pontuação"], reverse=True)

# colocacao = 0
# for k,v in jogadores_ordenados:
#   colocacao = colocacao+1
#   print(f"{colocacao}º Lugar: {k} com {v["pontuação"]}")

# from datetime import date, datetime

# Nome = input("Digite seu nome:")
# Data_Nascimento = input("Digite seu ano de nascimento (DD/MM/YYYY):")
# Data_Nascimento = datetime.strptime(Data_Nascimento, "%d/%m/%Y").date()
# Data_Atual = date.today()
# idade = Data_Atual.year - Data_Nascimento.year
# Carteira_Trabalho = int(input("Digite o número da sua carteira de trabalho:"))

# if (Data_Atual.month, Data_Atual.day) < (Data_Nascimento.month, Data_Nascimento.day):
#     idade -= 1

# cidadao = {
#     "Nome":Nome,
#     "Idade":idade,
#     "CPTS":Carteira_Trabalho
# }

# if Carteira_Trabalho != 0:
#     Ano_Contratacao = input("Insira o seu ano de contratação(YYYY):")
#     Ano_Contratacao_str = "01/01/"+Ano_Contratacao
#     Ano_Contratacao = datetime.strptime(Ano_Contratacao_str,"%d/%m/%Y").date()
#     Idade_Aposentadoria = idade + (35- (Data_Atual.year - Ano_Contratacao.year))
#     Salario = input("Insira o seu salário:")

#     cidadao["Ano Contratação"] = Ano_Contratacao_str
#     cidadao["Idade Aposentadoria"] = Idade_Aposentadoria
#     cidadao["Salario"] = Salario

# for k,v in cidadao.items():
#   print(f"{k} : {v}")


# Jogador = input("Nome do Jogador: ")
# Partidas = int(input(f"Quantas partidas {Jogador} jogou? "))

# Aproveitamento = {
#   "Nome": Jogador,
#   "Gols": [],
#   "Total": 0
# }

# for Partida in range(1,Partidas+1):
#   Gols = int(input(f"Quantos gols fez na partida {Partida}? "))
#   Aproveitamento["Gols"].append(Gols)
#   Aproveitamento["Total"] += Gols

# print(f"O jogador {Aproveitamento['Nome']} Jogou {Partidas} jogos, neles foram marcados as seguintes quantidades de gols:")
# Jogo = 1
# for Partida in Aproveitamento["Gols"]:
#   print(f"No jogo {Jogo} foram marcados {Partida} gols")
#   Jogo +=1

# print(f"No total foram {Aproveitamento['Total']} gols!")

# Continuar = "S"
# NumSequencia = 1
# Dados = []
# Lista_Mulheres = []
# Lista_Acima_media = []

# while Continuar == "S":
#   Nome = input("Nome: ")
#   Idade = int(input("Idade: "))
#   Sexo = input("Sexo:[M/F] ")
#   Sequencia = {
#     "Nome":Nome,
#     "Idade":Idade,
#     "Sexo":Sexo
#   }

#   Dados.append(Sequencia)
#   NumSequencia += 1
#   Continuar = input("Quer continuar?[S/N] ")

# Total = sum(1 for reg in Dados)

# Idade_Media = sum(pessoa["Idade"] for pessoa in Dados) / Total

# for Pessoa in Dados:
#   if Pessoa["Sexo"] == "F":
#     Lista_Mulheres.append(Pessoa["Nome"])

#   if Pessoa["Idade"] > Idade_Media:
#     Lista_Acima_media.append(Pessoa["Nome"])

# print(f"No total foram listadas {Total} pessoas")
# print(f"A média de idade é {Idade_Media}")
# print(f"Segue a lista com todas as mulheres {Lista_Mulheres}")
# print(f"Segue a lista com todas as pessoas que possuem a idade acima da média {Lista_Acima_media}")