# Solicitar las traducciones al usuario
entrada = input("Ingrese palabras en formato 'español:inglés' separadas por comas: ")

# Crear el diccionario de traducción
diccionario = {}
pares = entrada.split(",")
for par in pares:
    palabras = par.strip().split(":")
    if len(palabras) == 2:
        diccionario[palabras[0].strip()] = palabras[1].strip()

# Solicitar una frase en español
frase = input("Ingrese una frase en español para traducir: ")

# Traducir la frase palabra por palabra
traduccion = " ".join([diccionario.get(palabra, palabra) for palabra in frase.split()])

# Mostrar la traducción
print("Traducción:", traduccion)
