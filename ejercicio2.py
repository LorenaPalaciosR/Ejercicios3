"""2.- Desarrolla una función en Python que invierta una cadena de texto sin utilizar el operador de slicing.
El objetivo de este ejercicio es escribir una función que tome una cadena de caracteres y la devuelva invertida, 
pero sin hacer uso del operador de slicing ([::-1]). La función debe recorrer cada carácter de la cadena de entrada 
y construir una nueva cadena con los caracteres en orden inverso. Por ejemplo, si la función recibe "python", 
debe retornar "nohtyp". Asegúrate de no usar atajos como métodos incorporados que realicen la inversión por ti."""

def invertir_cadena(cadena):
    cadena_invertida = ""
    for caracter in cadena:
        cadena_invertida = caracter + cadena_invertida
    return cadena_invertida

palabra_usuario = input("Ingresa una palabra: ")

resultado = invertir_cadena(palabra_usuario)

print(f"La palabra invertida es: {resultado}")
 
