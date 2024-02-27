# El centro de salud de campuslands desea realizar un programa que le 
# permita calcular el IMC de los Estudiantes nuevos.
# IMC= peso(km)/(altura(m))*2
#nombre del estudiante
# la edad
# el imc 
# la categoría según el IMC obtenido
import os 
if __name__ == '__main__':
    newCalculo=True
    while newCalculo:
        nombre = input('Ingrese su nombre: ')
        edad = int(input('Ingrese su edad: '))
        peso = float(input('Ingrese su peso (Kg): '))
        altura = float(input('Ingrese su altura (m): '))
        IMC = peso / (altura**2)
        categoria = ''

        if 18.5 <= IMC <= 24.9:
            categoria = 'Normal'
        elif 25 <= IMC <= 29.9:
            categoria = 'Sobrepeso'
        elif 30 <= IMC <= 34.9:
            categoria = 'Obesidad I'
        elif 35 <= IMC <= 39.9:
            categoria = 'Obesidad II'
        elif IMC >= 40:
            categoria = 'Obesidad III'

        print(f'Nombre: {nombre}\nEdad: {edad}\nIMC: {IMC:.2f}\nCategoria: {categoria}\n')
        newCalculo=bool(input('Desea Ingresar Calcular otro IMC? s(SI) enter(No)'))



