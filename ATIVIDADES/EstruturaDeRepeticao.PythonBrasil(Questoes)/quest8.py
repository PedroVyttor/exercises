#Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0

for num in range(1, 6):
    n = float(input(f"Digite o {num}º número: "))
    soma += n

print(f"\nsoma: {soma}")
print(f"media: {soma / 5}")

