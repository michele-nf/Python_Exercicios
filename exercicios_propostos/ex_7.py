x = input("Qual o valor de x?")
y = input("Qual o valor de y?")
z = input("Qual o valor de z?")


def estaEntre(x, y, z):
    if y < x < z:
        return True
    else:
        return False


print(estaEntre(x, y, z))
