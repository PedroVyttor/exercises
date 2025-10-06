# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
# depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário
# Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os
# descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo
# abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

#Salário Bruto: (5 * 220) : R$ 1100,00
#(-) IR (5%) : R$ 55,00
#(-) INSS ( 10%) : R$ 110,00
#FGTS (11%) : R$ 121,00
#Total de descontos : R$ 165,00
#Salário Liquido : R$ 935,00


# Folha de Pagamento
valor_h = float(input('digite o valor da sua hora: '))
qtd_horas = float(input('digite a quantidade de horas trabalhadas no mes: '))
salario_bruto = valor_h * qtd_horas

if salario_bruto <= 900:
    ir = 0
    perc_ir = 0
elif salario_bruto <= 1500:
    ir = salario_bruto * 0.05
    perc_ir = 5
elif salario_bruto <= 2500:
    ir = salario_bruto * 0.10
    perc_ir = 10
else:
    ir = salario_bruto * 0.20
    perc_ir = 20

inss = salario_bruto * 0.10
sindicato = salario_bruto * 0.03
fgts = salario_bruto * 0.11

total_descontos = ir + inss + sindicato
salario_liquido = salario_bruto - total_descontos

print(f'salario Bruto: ({valor_h} * {qtd_horas}) : R$ {salario_bruto: }')
print(f'IR ({perc_ir}%) : R$ {ir: }')
print(f'INSS (10%) : R$ {inss: }')
print(f'sindicato (3%) : R$ {sindicato: }')
print(f'FGTS (11%) : R$ {fgts: }')
print(f'total de descontos : R$ {total_descontos: }')
print(f'salario liquido : R$ {salario_liquido: }')
