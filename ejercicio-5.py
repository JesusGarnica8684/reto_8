def potencia_recursiva(n: int, p: int) -> int:
    # en caso de la potencia ser a la cero se pone el caso base
    if p == 0:
        return 1
    # se organiza el caso recursivo como n^p = n * n^(p-1)
    # se puede entender como que cada vez que la función se llama a si misma se multiplica con su potencia anterior
    return n * potencia_recursiva(n, p - 1)

if __name__=="__main__":
    base = int(input("Ingrese la base a potenciar: "))
    exponente = int(input("Ingrese el exponente: "))
    potencia = potencia_recursiva(base, exponente)
    print (potencia)
    print (base**exponente) #linea de comprobacion de resultados 