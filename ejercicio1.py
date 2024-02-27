# Se requiere realizar un programa en Python que permita leer 3 
#números enteros positivos e imprima La sumatoria de los tres números.
def numerosEnteros():
    try:
        entero = int(input('Ingrese un numero entero: '))
        if entero > 0:
            return entero
        else:
            print('El numero debe ser mayor a 0')
            return numerosEnteros()
    except ValueError:
        print('Numero no válido')
        return numerosEnteros()

if __name__ == '__main__':
    enteros = []
    suma = 0

    for i in range(3):  
        numero = numerosEnteros()
        enteros.append(numero)
        suma += numero

    print("Lista de números ingresados:", enteros)
    print("La suma de los números es:", suma)

    


 

