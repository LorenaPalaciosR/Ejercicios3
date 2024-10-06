"""4. Crea una función que determine si una palabra o frase es un palíndromo, ignorando mayúsculas y espacios.
Un palíndromo es una palabra o frase que se lee igual de adelante hacia atrás y de atrás hacia adelante, 
ignorando espacios y mayúsculas. Por ejemplo, "Anita lava la tina" es un palíndromo. 
Escribe una función que reciba una cadena de caracteres y determine si es un palíndromo. 
La función debe ser capaz de ignorar los espacios y no diferenciar entre letras mayúsculas y minúsculas. 
Debes recorrer la cadena y comparar sus caracteres de manera inversa sin usar el método de slicing ([::-1])."""
def es_palindromo(cadena):
    #Limpiar la cadena: quitar espacios y convertir a minúsculas
    cadena_limpia ="".join(cadena.split()).lower()
    
    #Longitud de la cadena limpia
    longitud = len(cadena_limpia)
    
    #Comparar caracteres desde el inicio y el final
    for i in range(longitud // 2):
        if cadena_limpia[i] != cadena_limpia[longitud - 1 - i]:
           return f´´"{cadena}" no es un palíndromo.´
    
    return f´"(cadena)" es un palíndromo.´

#Ejemplo de uso
frase = "Anita lava la tinta"
print(es_palindromo(frase)) #Salida: "Anita lava la tinta" es un palíndromo.
  
              