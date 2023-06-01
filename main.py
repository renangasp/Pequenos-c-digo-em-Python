valorPorHora = float(input("Qual o valor que você ganhou? "))
horasTrabalhadas = int(input("Quantas horas você trabalhou? "))
salario = horasTrabalhadas * valorPorHora
print("Nesse mês você vai receber R$ {0:.2f}".format(salario))
#a linha acima que tem o simbolo {0:.2f}
# 0 zero quer dizer a ordem que os dados da variavel aparecerá
# o ponto é obrigatório e o "2F" diz respeito
# as casas decimais de numero quebrado ou float em python