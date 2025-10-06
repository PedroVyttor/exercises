#As Organizações Tabajara resolveram dar um aumento de salário aos
# seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o
# reajuste segundo o seguinte critério, baseado no
#salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5%
#
#Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.



sal = float(input('Digite seu salário: '))

if sal <= 280:
    reaj = sal * 1.20 #aumento de 20%
    porc = 20

if sal > 280 and sal <=700:
    reaj = sal * 1.15 #aumento de 15%
    porc =  15

if sal > 700 and sal <= 1500:
    reaj = sal * 1.1 #aumento de 10%
    porc = 10

if sal >= 1500:
    reaj = sal * 1.05 #aumento de 5%
    porc =  5

print('o salario antes do reajuste: R$ ' ,sal)
aumento = reaj - sal
sal_atual = reaj + sal
print('o aumento foi de: ' ,  aumento, '%')
print('o novo salario: R$' ,sal_atual)