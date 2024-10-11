"""5.- Desarrolla una función que sume los dígitos de un número de manera recursiva hasta obtener un solo dígito.
Dado un número entero positivo, suma sus dígitos repetidamente hasta que el resultado sea un solo dígito. 
Por ejemplo, para el número 9876, sumamos 9 + 8 + 7 + 6 = 30, luego sumamos 3 + 0 = 3. 
Escribe una función recursiva que tome un número entero positivo y devuelva el resultado de esta suma repetida.
La función debe manejar correctamente números de varias cifras y realizar las llamadas recursivas necesarias."""

# Elaborado por Carlos


def suma_digitos(n):
    if n < 10:
        return n
    else:

        suma = sum(int(digit) for digit in str(n))
        return suma_digitos(suma)


try:
    numero = int(input("Introduce un número entero positivo: "))
    if numero < 0:
        print("Por favor, ingresa un número entero positivo.")
    else:
        resultado = suma_digitos(numero)
        print(
            f"La suma de los dígitos de {numero} hasta un solo dígito es: {resultado}"
        )
except ValueError:
    print("Entrada no válida. Asegúrate de ingresar un número entero.")
