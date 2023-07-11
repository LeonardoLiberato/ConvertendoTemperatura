#Desafio 14
#escreva um programa que converte uma temperatura digitada em C e converta para F
#
#exercicio 1

ce = float(input("Informe a temperatura em C"))
fa = 9*ce/5+32
print('A temperatura de {}C corresponde a {}F.'.format(ce,fa))

#
#exercicio 2
#
ce = float(input("Informe a temperatura em C"))
fa = ((9*ce)/5)+32
print('A temperatura de {}C corresponde a {}F.'.format(ce,fa))

#etapas de calculo de C para F
#9xC = resultado
#resultado dividido por 5
#resultado da divisao =32
#
# 9 x 36.8c = 331.2
# 331.2 / 5 = 66.24
# 66.24 + 32 =98.24
