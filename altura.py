altura = float (input("Informe sua altura: "))
sexo = input("Informe o sexo m/f: ")
if sexo.lower() == 'm':
    pesoIdeal = (72.7 * altura) - 58
elif sexo.lower() == 'f':
    pesoIdeal = (62.1 * altura) - 44.7
else:
    pesoIdeal = 0
    print("Sexo não reconhecido.")
print("Seu peso ideal é {0:.2f}".format(pesoIdeal))
