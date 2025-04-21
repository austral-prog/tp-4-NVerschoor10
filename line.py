import math

def line():
    a = float(input("Ingrese el coeficiente A: "))
    b = float(input("Ingrese el coeficiente B: "))
    x1 = float(input("Ingrese el coeficiente X1: "))
    x2 = float(input("Ingrese el coeficiente X2: "))

    print("El coeficiente A de su ecuación de la recta es: {:.1f}".format(a))
    print("El coeficiente B de su ecuación de la recta es: {:.1f}".format(b))
    print("El coeficiente X1 de su ecuación de la recta es: {:.1f}".format(x1))
    print("El coeficiente X2 de su ecuación de la recta es: {:.1f}".format(x2))
    
    print()
    print("Para la siguiente ecuación:")
    print("\tY = {:.1f}X + {:.1f}".format(a, b))
    print()
    
    y1 = a * x1 + b
    y2 = a * x2 + b

    print("Dados los siguientes puntos:")
    print("\tP1 ({:.1f}, {})".format(x1, y1))
    print("\tP2 ({:.1f}, {})".format(x2, y2))
    print()

    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    print("La distancia entre ellos es: {}".format(distancia))
    print("HINT: Formula de la distancia")
    print("HINT: Python Math doc")

