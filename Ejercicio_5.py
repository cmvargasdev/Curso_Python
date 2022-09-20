def esBisiesto (anio:int):
    if (anio % 400 == 0):
        print('El año:' + str(anio) + ' es bisiesto ')
    elif (anio % 100 == 0):
        print('El año:' + str(anio) + ' NO es bisiesto ')
    elif (anio % 4 == 0):
        print('El año:' + str(anio) + ' es bisiesto ')
    else:
        print('El año:' + str(anio) + ' NO es bisiesto ')

esBisiesto(2004)
