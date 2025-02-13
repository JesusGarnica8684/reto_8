#Realice pruebas para calcular fibonacci con iteración o con recursión. 
#Determine desde que número de la serie la diferencia de tiempo se vuelve significativa. 
import timeit 

def fibonacci(n: int) -> int:
    #calcula el número de Fibonacci en la posición n
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1 # se inicializa las variables a y b con los valores f(0)=0 y f(1)=1
    for _ in range(2, n + 1):#no se va utilizar el indice de for, asi que el guion le pide al codigo que lo ignore
        # la formula de fibonacci es igual a f(n) = f(n−1) + f(n−2)       
        a, b = b, a + b # a y b se actualizan para calcular el siguiente número de Fibonacci
    return b #valor de fibonacci en la posición n

if __name__=="__main__":
    tiempo = timeit.repeat("fibonacci(35)", "from __main__ import fibonacci", number=100000)
    print(tiempo)