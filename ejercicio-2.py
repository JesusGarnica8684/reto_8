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