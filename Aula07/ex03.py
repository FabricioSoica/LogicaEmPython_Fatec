soma = 0
qnt =int(input(f"digite quantas idades serão calculadas: "))
for i in range(1, qnt+1):
    n = int(input(f"entre com a {i}ª idade: "))
    soma = soma = n
media = soma / qnt
print(f"A média das idades é {media:5.2f}")
