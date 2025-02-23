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

if divisa in monedas:
    tasa_cambio = monedas[divisa]
    print(f"1 {divisa} equivale a {tasa_cambio} pesos colombianos")
    
    try:
        cantidad = float(input("Ingrese la cantidad a convertir: "))
        conversion = cantidad * tasa_cambio
        print(f"{cantidad} {divisa} equivalen a {conversion} pesos colombianos")
    except ValueError:
        print("Error: Debe ingresar un número válido")
else:
      print("La divisa ingresada no está en la lista")
