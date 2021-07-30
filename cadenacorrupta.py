cadena_corrupta = "airotsiH,6.7,aícraG nómaR"

#solucion
cadena_volteada = cadena_corrupta[::-1]
nombre          = cadena_volteada[:12]
nota            = cadena_volteada[13:16]
materia         = cadena_volteada[17:]
cadena_formateada = nombre + " ha sacado un " + nota + " en " + materia + "."
print(cadena_formateada)
print(cadena_volteada)
print(nombre)
