# 4. Se desea realizar un programa en Python que permita ingresar n números enteros positivos y cuando se
# Ingrese un numero negativo debe mostrar en pantalla el siguiente reporte.
# a. Total de números ingresados
# b. Total de números pares ingresados
# c. Promedio de los números pares
# d. Promedio de los números impares
# e. Cuantos números son menores que 10
# f. Cuantos números están entre 20 y 50
# g. Cuantos números son mayores que 100
if __name__ == '__main__':
    n = 0
    totalPares = 0
    totalImpares = 0
    menores10 = 0
    entre50y20 = 0
    mayores100 = 0

    while True:
        
        numero = int(input('Ingrese un Numero entero Positivo (Ingrese un número negativo para finalizar): '))
        
        if numero > 0:
            n += 1

            if numero % 2 == 0:
                totalPares += 1
            else:
                totalImpares += 1

            if numero < 10:
                menores10 += 1
            elif 20 <= numero <= 50:
                entre50y20 += 1
            elif numero > 100:
                mayores100 += 1
        else:
            break

    porPares = totalPares / n if n > 0 else 0
    porImpares = totalImpares / n if n > 0 else 0

    print("Total de números ingresados:", n)
    print("Total de números pares:", totalPares)
    print("Porcentaje de números pares:", porPares)
    print("Total de números impares:", totalImpares)
    print("Porcentaje de números impares:", porImpares)
    print("Números menores que 10:", menores10)
    print("Números entre 20 y 50:", entre50y20)
    print("Números mayores que 100:", mayores100)

            


