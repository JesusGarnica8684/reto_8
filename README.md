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
4. Escriba una función recursiva para calcular la operación de la potencia.
5. Utilice la siguiente plantilla de code para contar el tiempo:
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
