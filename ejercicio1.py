"""1.- Escribe una función en Python que determine si un número es perfecto.
Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos (excluyendo el número mismo). 
Por ejemplo, el número 6 es perfecto porque sus divisores (1, 2 y 3) suman 6. 
Escribe una función que reciba un número entero positivo y devuelva un mensaje indicando si el número es perfecto o no. 
Tu implementación debe recorrer todos los posibles divisores menores al número dado, 
calcular su suma y luego verificar si esta suma es igual al número original."""
def es_numero_perfecto(n):
    if n <= 0:
        return "El número debe ser un entero positivo."
    
    suma_divisiones = 0
    for i in range(1,n):
        if n % i == 0:
            suma_divisiones += i
            
        
    if suma_divisiones == n:
        return f"{n} es un número perfecto."
    else: 
        return f"{n} no es un número perfecto."
    
    #Ejemplo de uso
    numero = 6
    print(es_numero_perfecto(numero)) #Salida: 6 es un número perfecto.
    