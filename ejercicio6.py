"""6.- Implementa una función que calcule la media, mediana y moda de una lista de números.
Dada una lista de números enteros o flotantes, escribe una función que calcule y devuelva la media, 
la mediana y la moda de la lista. La media es el promedio de los números, la mediana es el valor que 
separa la mitad superior de la inferior cuando la lista está ordenada, y la moda es el número que más veces aparece en la lista. 
Asegúrate de manejar correctamente los casos en que no haya una moda única o cuando la lista sea vacía.
Para este ejercicio, puedes asumir que siempre habrá al menos un número en la lista."""
from collections import Counter
import statistics

def calcular_estadisticas(lista):
    if not lista:
        return None, None, None  # Manejar caso de lista vacía

    # Media
    media = sum(lista) / len(lista)

    # Mediana
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    if n % 2 == 0:
        mediana = (lista_ordenada[n//2 - 1] + lista_ordenada[n//2]) / 2
    else:
        mediana = lista_ordenada[n//2]

    # Moda
    contador = Counter(lista)
    max_frecuencia = max(contador.values())
    modas = [num for num, freq in contador.items() if freq == max_frecuencia]

    if len(modas) == len(contador):
        moda = None  # Sin moda única
    else:
        moda = modas[0]  # Retornamos la primera moda encontrada

    return media, mediana, moda

# Ejemplo de uso
numeros = [1, 2, 2, 3, 4]
media, mediana, moda = calcular_estadisticas(numeros)
print(f"Media: {media}, Mediana: {mediana}, Moda: {moda}")
