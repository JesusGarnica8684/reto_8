import math

def promedio(*args) -> float:
    sum : float = 0 # se separa la suma en una variable que se inicializa en 0
    count : int = 0 # contador de cantidad de argumentos que ingresaron  
    for num in args: 
        sum += num # se suma hasta completar todos los argumentos 
        count += 1 
    prom = sum / count # se divide la suma sobre los argumentos contados 
    return prom

def raiz_tres(*args) -> float:
    menor = min(args)
    raiz_cubica = menor ** (1/3)
    return raiz_cubica

def promedio_multiplicativo(*args) -> float:
    por : float = 1 # se separa la multiplicación de los números en una variable inicializada en 1
    count : int = 0 # contador de cantidad de argumentos que ingresaron  
    for num in args: 
        por *= num # se multiplica hasta completar todos los argumentos 
        count += 1 
    prom_multi = math.pow(por, 1/count) # Calcular la raíz según el contador 
    return prom_multi

if __name__ == "__main__":

    numA = int(input("Ingrese numero a: "))
    numB = int(input("Ingrese numero b: "))
    numC = int(input("Ingrese numero c: "))
    numD = int(input("Ingrese numero d: "))
    numE = int(input("Ingrese numero e: "))
#promedio 
    print("Promedio de ", numA, numB, " = ", (promedio(numA, numB)))
    print("Promedio de ", numA, numB , numC, " = ", (promedio(numA, numB, numC)))
    print("Promedio de ", numA, numB , numC, numD, " = ", (promedio(numA, numB, numC, numD)))
    print("Promedio de ", numA, numB , numC, numD, numE, " = ", (promedio(numA, numB, numC, numD, numE)))
#raíz cúbica del menor numero
    print("Raiz cubica del menor numero entre ", numA, numB, " = ", (raiz_tres(numA, numB)))
    print("Raiz cubica del menor numero entre ", numA, numB , numC, " = ", (raiz_tres(numA, numB, numC)))
    print("Raiz cubica del menor numero entre ", numA, numB , numC, numD, " = ", (raiz_tres(numA, numB, numC, numD)))
    print("Raiz cubica del menor numero entre ", numA, numB , numC, numD, numE, " = ", (raiz_tres(numA, numB, numC, numD, numE)))
#promedio multiplicativo
    print("Promedio multiplicativo de ", numA, numB, " = ", (promedio_multiplicativo(numA, numB)))
    print("Promedio multiplicativo de ", numA, numB , numC, " = ", (promedio_multiplicativo(numA, numB, numC)))
    print("Promedio multiplicativo de ", numA, numB , numC, numD, " = ", (promedio_multiplicativo(numA, numB, numC, numD)))
    print("Promedio multiplicativo de ", numA, numB , numC, numD, numE, " = ", (promedio_multiplicativo(numA, numB, numC, numD, numE)))