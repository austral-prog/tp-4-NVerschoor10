import math
def line():
    a = float(input("Ingrese el coeficiente A: "))
    b = float(input("Ingrese el coeficiente B: "))
    x1 = float(input("Ingrese el coeficiente X1: "))
    x2 = float(input("Ingrese el coeficiente X2: "))
    print(f"El coeficiente A de su ecuación de la recta es: {a}")
    print(f"El coeficiente B de su ecuación de la recta es: {b}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {x1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {x2}")
    print("")
    print("Para la siguiente ecuación:")
    print(f"\tY = {a}X + {b}")
    print("")
    print("Dados los siguientes puntos:")

    a,b,x1,x2 = float(a),float(b),float(x1),float(x2)

    #Cuentas
    y1 = a*x1 + b
    y2 = a*x2 + b


    print(f"\tP1 ({x1}, {y1})")

    print(f"\tP2 ({x2}, {y2})")
    print("")
    p1 = [x1,y1]
    p2 = [x2,y2]
    distancia = math.dist(p2,p1) 
    print(f"La distancia entre ellos es: {distancia}")
