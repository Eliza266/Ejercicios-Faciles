# El centro de salud de campuslands desea realizar un programa que le 
# permita calcular el IMC de los Estudiantes nuevos.
# IMC= peso(km)/(altura(m))*2
#nombre del estudiante
# la edad
# el imc 
# la categoría según el IMC obtenido
# Se deben registrar 20 Estudiantes
# a. Cuantos estudiantes se encuentran en el peso ideal.
# b. Cuantos estudiantes se encuentran en obesidad grado I
# c. Cuantos estudiantes se encuentran en obesidad grado II
# d. Cuantos estudiantes se encuentran en obesidad grado III
# e. Cuantos estudiantes se encuentran en Sobrepeso
from tabulate import tabulate
import os
if __name__ == '__main__':
    listaEstudiantes=[]
    normal=0
    sobrepeso=0
    obI=0
    obII=0
    obIII=0
    for i in range(20):
        nombre = input('Ingrese su nombre: ')
        edad = int(input('Ingrese su edad: '))
        peso = float(input('Ingrese su peso (Kg): '))
        altura = float(input('Ingrese su altura (m): '))
        IMC =(peso / (altura**2))
        IMC_redondeado = round(IMC, 2)
        categoria = ''
        if 18.5 <= IMC <= 24.9:
            categoria = 'Normal'
            normal+=1
        elif 25 <= IMC <= 29.9:
            categoria = 'Sobrepeso'
            sobrepeso+=1
        elif 30 <= IMC <= 34.9:
            categoria = 'Obesidad I'
            obI+=1
        elif 35 <= IMC <= 39.9:
            categoria = 'Obesidad II'
            obII+=1
        elif IMC >= 40:
            categoria = 'Obesidad III'
            obIII+=1
        listaEstudiantes.append([nombre,edad,IMC_redondeado,categoria])
        
        print(f'Nombre: {nombre}\nEdad: {edad}\nIMC: {IMC:.2f}\nCategoria: {categoria}\n')
        os.system('cls')
    headers = ["Nombre", "Edad", "IMC", "Categoría"]
    print(tabulate(listaEstudiantes, headers=headers, tablefmt="grid"))

    # Imprimir estadísticas
    print(f"\nEstadísticas:")
    print(f"Normal: {normal}")
    print(f"Sobrepeso: {sobrepeso}")
    print(f"Obesidad I: {obI}")
    print(f"Obesidad II: {obII}")
    print(f"Obesidad III: {obIII}")


