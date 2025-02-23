# Solicitar datos al usuario
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
direccion = input("Ingrese su dirección: ")
telefono = input("Ingrese su número de teléfono: ")

# Guardar en un diccionario
usuario = {
    "Nombre": nombre,
    "Edad": edad,
    "Dirección": direccion,
    "Teléfono": telefono
}

# Mostrar mensaje
print(f"{usuario['Nombre']} tiene {usuario['Edad']} años, vive en {usuario['Dirección']} y su número de teléfono es {usuario['Teléfono']}")
