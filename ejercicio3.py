"""3.- Escribe una función que calcule el factorial de un número entero de forma iterativa.
El factorial de un número n (denotado como n!) es el producto de todos los números enteros positivos desde 1 hasta n. 
Por ejemplo, el factorial de 5 es 5! = 5 × 4 × 3 × 2 × 1 = 120. Escribe una función que reciba un número entero positivo 
y devuelva su factorial. Debes implementar la función usando un bucle for, 
multiplicando el valor de cada número por el resultado acumulado. Además, considera casos en los que el número sea 0 o negativo."""

def factorial(n):
    if n < 0:
        return "Error: El factorial no está definido para números negativos."
    
    resultado = 1
    
    calculo = f"{n}! = "
    
    for i in range(n, 0, -1):
        resultado *= i
        calculo += f"{i} × " if i > 1 else f"{i} = "

    calculo += str(resultado)
    return calculo

numero = int(input("Ingrese un numero entero positivo: "))
print(factorial(numero))
