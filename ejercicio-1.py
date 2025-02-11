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
