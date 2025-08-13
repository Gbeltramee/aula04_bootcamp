def calcula_bonus_kpi (nome:str, salario:float, bonus:float) :
  bonus_recebido: float = 1000 + salario * bonus

  lista_valores = {
    "nome":nome,
    "salario":salario,
    "bonus_percetual":bonus,
    "bonus_recebido":bonus_recebido
  }
  print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_recebido:.2f}.")
  
  return lista_valores