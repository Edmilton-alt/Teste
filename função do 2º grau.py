from math import gcd
#Atribuindo os valores de a, b e c da função de segundo grau
a = int(input("Digite aqui o valor de a: "))
b = int(input("Digite aqui o valor de b: "))
c = int(input("Digite aqui o valor de c: "))

#pegando o mdc dos números pra reuzir pro menor número possível
mdc = int(gcd(a, b, c))

a1 = a/mdc
b1 = b/mdc
c1 = c/mdc

#calculo do delta
delta = b1**2 - 4*a1*c1

v1 = round((-b1/(2*a1)), 2)
v2 = round((-(delta)/(4*a1)), 2)

#Se delta for menor que zero, então fala uma coisa ai se ele for maior fala outra
if delta < 0:
    print(f"As raízes da função ({a}x²) + ({b}x) + ({c}) não existem")
    print(f"E o X e Y do vértice são, respectivamente {v1} e {v2}")
else:
    x1 = round(((-b1+(delta**(1/2)))/2*a1), 2)
    x2 = round(((-b1-(delta**(1/2)))/2*a1), 2)
    print(f"As raízes da função ({a}x²) + ({b}x) + ({c}) são {x1} e {x2}")
    print(f"E o X e Y do vértice são, respectivamente {v1} e {v2}")
