def main():
    compradores = {}
    stock_funcion = {1: 150, 2: 180}
    vendidos_funcion = {1: 0, 2: 0}

    while True:
        print("\nTOTEM AUTOATENCIÓN CAFECONLECHE")
        print("1.- Comprar entrada a Cats")
        print("2.- Cambio de función")
        print("3.- Mostrar stock de funciones")
        print("4.- Salir")

        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            comprar_entrada(compradores, stock_funcion, vendidos_funcion)
        elif opcion == "2":
            cambiar_funcion(compradores, stock_funcion, vendidos_funcion)
        elif opcion == "3":
            mostrar_stock(stock_funcion, vendidos_funcion)
        elif opcion == "4":
            print("Programa terminado...")
            break
        else:
            print("Debe ingresar una opción válida!")

def comprar_entrada(compradores, stock, vendidos):
    nombre = input("Nombre del comprador: ").strip()
    if nombre in compradores:
        print("El nombre del comprador ya fue registrado.")
        return

    print("Seleccione función:")
    print("1: Cats Día Viernes")
    print("2: Cats Día Sábado")
    try:
        funcion = int(input("Ingrese opción: "))
        if funcion not in (1, 2):
            print("Opción de función inválida.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    if (funcion == 1 and vendidos[1] >= 150) or (funcion == 2 and vendidos[2] >= 180):
        print("No hay entradas disponibles para esta función.")
        return

    compradores[nombre] = funcion
    vendidos[funcion] += 1
    print("Entrada registrada exitosamente.")

def cambiar_funcion(compradores, stock, vendidos):
    nombre = input("Nombre del comprador: ").strip()
    if nombre not in compradores:
        print("El comprador no existe.")
        return

    actual = compradores[nombre]
    nueva = 2 if actual == 1 else 1

    if (nueva == 1 and vendidos[1] >= 150) or (nueva == 2 and vendidos[2] >= 180):
        print("No hay stock disponible para la otra función.")
        return

    compradores[nombre] = nueva
    vendidos[actual] -= 1
    vendidos[nueva] += 1
    print("Cambio de función exitoso.")

def mostrar_stock(stock, vendidos):
    print("Stock de Funciones:")
    print(f"Función 1 (Viernes): Disponibles {150 - vendidos[1]}, Vendidas {vendidos[1]}")
    print(f"Función 2 (Sábado): Disponibles {180 - vendidos[2]}, Vendidas {vendidos[2]}")

if __name__ == "__main__":
    main()
