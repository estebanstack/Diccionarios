# Diccionario con tasas de cambio
monedas = {
    'Euro': 4444,
    'Dollar': 4422,
    'Yen': 31.86,
    'Libra': 5140,
    'Franco Suizo': 4970,
    'Dólar Canadiense': 3300,
    'Dólar Australiano': 2900,
    'Real Brasileño': 850,
    'Peso Mexicano': 240,
    'Peso Argentino': 12.5
}

# Solicitar divisa al usuario
divisa = input("Ingrese el nombre de la divisa: ").strip()

# Verificar si la divisa está en el diccionario
if divisa in monedas :
    cantidad = float(input(f"Ingrese la cantidad de {divisa} a convertir: "))
    conversion = cantidad * monedas[divisa]
    print(f"{cantidad} {divisa} equivale a {conversion} pesos colombianos.")
else:
    print("La divisa ingresada no está en el diccionario.")
