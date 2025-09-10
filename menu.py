ventas=[]
def crear_venta():
    id = input("Ingrese el ID del producto: ")
    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad de producto: "))
    precio_unitario = float(input("Ingrese el precio del producto: "))
    ventas.append([id, producto, cantidad, precio_unitario])
    print("Venta registrada exitosamente")

def listar_ventas():
    if not ventas:
        print("No hay ventas registradas.\n")
        return
    for venta in ventas:
        print(f"ID: {venta[0]}, Producto: {venta[1]}, Cantidad: {venta[2]}, Precio Unitario: {venta[3]}")
    print()

def buscar_por_id():
    id = input("Ingrese el ID de la venta a buscar: ")
    for venta in ventas:
        if venta[0] == id:
            print(f"Venta encontrada: {venta}")
            return
    print("Venta no encontrada.\n")

def modificar_venta():
    id = input("Ingrese el ID de la venta a modificar: ")
    for venta in ventas:
        if venta[0] == id:
            producto = input("Nuevo producto: ")
            cantidad = int(input("Nueva cantidad: "))
            precio_unitario = float(input("Nuevo precio unitario: "))
            venta[1] = producto
            venta[2] = cantidad
            venta[3] = precio_unitario
            print("Venta modificada correctamente.\n")
            return
    print("Venta no encontrada.\n")

def eliminar_venta():
    id = input("Ingrese el ID de la venta para eliminarla: ")
    for i in range(len(ventas)):
        if ventas[i][0] == id:
            del ventas[i]
            print("Venta eliminada correctamente.\n")
            return
    print("Venta no encontrada.\n")

def calcular_totales():
    total = 0
    for venta in ventas:
        total += venta[2] * venta[3] 
    print(f"Ingreso total: ${total:.2f}\n")

def menu():
    while True:
        print("---- MENÚ DE OPCIONES ----")
        print("1. Crear nueva venta")
        print("2. Listar ventas")
        print("3. Buscar por ID")
        print("4. Modificar")
        print("5. Eliminar")
        print("6. Calcular totales (ingreso total)")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_venta()
        elif opcion == "2":
            listar_ventas()
        elif opcion == "3":
            buscar_por_id()
        elif opcion == "4":
            modificar_venta()
        elif opcion == "5":
            eliminar_venta()
        elif opcion == "6":
            calcular_totales()
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.\n")

# Ejecutar el menu de opciones
menu()