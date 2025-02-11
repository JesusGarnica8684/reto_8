if __name__ == "__main__":
    Capita = float(input("Ingrese el monto inicial del prestamo: "))
    int_anual = float(input("Ingrese la tasa de interes anual sin el simbolo porcentaje: "))
    meses = int(input("Ingrese el número de meses que se llevará el prestamo: "))
    #funcion para calcular el interes compuesto
    valorFinal = (lambda p, i, n: p * (1 +(i/100/12)) **n)(Capita, int_anual, meses)
    # el interes i se convierte a interés a mensual. Con la formula de interes
    # compuesto se calcula a que valor llegara el prestamo tras los n meses
    print("El valor final del préstamo después de ", meses ," meses es: ", valorFinal)