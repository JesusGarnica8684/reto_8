# Reto 8

1. De los retos anteriores selecione 3 funciones y escribalas en forma de lambdas.
* Código para calcular el volumen total y area total de la siguiente figura:
![image](https://github.com/user-attachments/assets/8300fa43-7ae4-494d-9cff-82b22d296726)
```python
from math import pi, sqrt #se trae de la libreria math especificamente los dos modulos que serán utilizados

if __name__=="__main__":
    #se ingresan por teclado las dimensiones de las figuras 
    radioE = float(input("Ingrese el radio de la esfera. "))
    radioC = float(input("Ingrese el radio de la base del cono. "))
    alturaC = float(input("Ingrese la altura del cono. "))
    #calcular_sólidos 
    calc_earea = (lambda r1: 4*pi*(r1**2))(radioE) #area de la esfera 
    calc_evol = (lambda r1: 4/3*pi*(r1**2))(radioE) #volumen de la esfera
    calc_gcono = (lambda r2, h: sqrt((r2**2)+(h**2)))(radioC, alturaC) #geriatriz del cono
    calc_carea = (lambda r2, gc : pi*r2*(r2+gc))(radioC, calc_gcono) #area del cono
    calc_cvol = (lambda r2, h: 1/3*pi*(r2**2)*h)(radioC, alturaC) #volumen del cono
    a_total = (lambda a1, a2: a1 + a2)(calc_carea, calc_earea)
    v_total = (lambda a1, a2: a1 + a2)(calc_cvol, calc_evol)

    print("El area total de los sólidos es: ", a_total, "\nEl volumen total de los sólidos es: ", v_total)

```
* Código para calcular cantidad de carne de gallinas, gallos y pollitos.
```python
if __name__=="__main__":
    nGallinas = int(input("Ingrese el número de gallinas que tiene: "))
    nGallos = int(input("Ingrese el número de gallos que tiene: "))
    nPollitos = int(input("Ingrese el número de pollitos que tiene: "))
    carGallina = (lambda n: n*6)(nGallinas)
    carGallo = (lambda n: n*7)(nGallos)
    carPollito = (lambda n: n*1)(nPollitos)
    print ("Para un numero de ", nGallinas, " gallinas, hay una cantidad de carne de ", carGallina,"Kg")
    print ("Para un numero de ", nGallos, " gallos, hay una cantidad de carne de ", carGallo,"Kg")
    print ("Para un numero de ", nPollitos, " pollitos, hay una cantidad de carne de ", carPollito,"Kg")
```
* Función para calcular el valor de un préstamo C usando interés compuesto del i por n meses
```python
if __name__ == "__main__":
    Capita = float(input("Ingrese el monto inicial del prestamo: "))
    int_anual = float(input("Ingrese la tasa de interes anual sin el simbolo porcentaje: "))
    meses = int(input("Ingrese el número de meses que se llevará el prestamo: "))
    #funcion para calcular el interes compuesto
    valorFinal = (lambda p, i, n: p * (1 +(i/100/12)) **n)(Capita, int_anual, meses)
    # el interes i se convierte a interés a mensual. Con la formula de interes
    # compuesto se calcula a que valor llegara el prestamo tras los n meses
    print("El valor final del préstamo después de ", meses ," meses es: ", valorFinal)
```

3. De los retos anteriores selecione 3 funciones y escribalas con argumentos no definidos (*args).

```python
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
```

5. Escriba una función recursiva para calcular la operación de la potencia.
```python
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
```
7. Utilice la siguiente plantilla de code para contar el tiempo:
```python
import time

start_time = time.time()
# instrucciones sobre las cuales se quiere medir tiempo de ejecución
end_time = time.time()

timer = end_time - start_time
print(timer)
```

Realice pruebas para calcular fibonacci con iteración o con recursión. Determine desde que número de la serie la diferencia de tiempo se vuelve significativa.
**Importante:** Revisar este [hilo](https://stackoverflow.com/questions/8220801/how-to-use-timeit-module).

5. Crear cuenta en [stackoverflow](https://stackoverflow.com/) y adjuntar imagen en el repo

6. Cosas de adultos....ir a [linkedin](https://www.linkedin.com/) y crear perfil....NO IMPORTA que estén iniciando, si tienen tiempo para redes poco útiles como fb, insta, o tiktok tienen tiempo para crear un perfil mamalón. Dejar enlace en el repo.
