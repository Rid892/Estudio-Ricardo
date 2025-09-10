def leer_csv(nombre_archivo):
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        lineas= f.read().strip().split("\n")
        datos=[linea.split(",") for linea in lineas]
    return datos

def escribir_csv(nombre_archivo, encabezado, filas):
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(",".join(str(x) for x in fila) + "\n")

def seleccion_sort(lista, key_func=lambda x: x, reverse=False):
    n= len(lista)
    for i in range(n):
        idx_extremo = i
        for j in range(i+1, n):
            if reverse:
                if key_func(lista[j]) > key_func(lista[idx_extremo]):
                    idx_extremo= j
            else:
                if key_func(lista[j]) < key_func(lista[idx_extremo]):
                    idx_extremo = j
                lista[i], lista[idx_extremo]= lista[idx_extremo], lista[i]
    return lista

#Opcion 1
def ver_los_libros_ordenados():
    datos= leer_csv("libros.csv")
    encabezado, filas = datos[0], datos[1:]
    filas= seleccion_sort(filas, key_func=lambda x: int(x[4]))
    print("Libros ordenados por anios ")
    for fila in filas:
        print(f"{fila[1]}, {fila[2]}, {fila[3]}, {fila[4]}, {fila[5]}")
        
#Opcion 2
def agregar_nuevo_usuario():
    datos= leer_csv("usuarios.csv")
    encabezado, filas = datos[0], datos[1:]
    nuevo_id=max(int(f[0]) for f in filas) + 1
    nombre= input("Nombre del usuario: ")
    email= input("Agregue el email del usuario: ")
    filas.append([str(nuevo_id), nombre, email])
    escribir_csv("usuarios.csv", encabezado, filas)
    print("Usuario agregado con id={nuevo_id}.")
    
#Opcion 3
def calcular_total_prestamos_por_libro():
    libros= leer_csv("libros.csv")
    prestamos = leer_csv("prestamos.csv")
    encabezado_libros, filas_libros = libros[0], libros[1:]
    encabezado_prestamos, filas_prestamos = prestamos[0], prestamos[1:]
    
    totales= {}
    for fila in filas_libros:
        libro_id, titulo = fila[0], fila [1]
        if libro_id in totales:
            resultados.append([libro_id, titulo, totales[libro_id]])

totales= {}
for fila in filas_prestamos:
    libro_id, cantidad= fila[2], int(fila[3])
    totales[libro_id]= totales.get(libro_id, 0) + cantidad
resultados= []
for fila in filas_libros:
    
    

def menu():
    while True:
        print("---- MENÚ DE OPCIONES ----")
        print("1. Ver libros ordenados por año de publicación (ascendente).")
        print("2. Nuevo usuario")
        print("3. total prestamos por libro")
        print("4. Usuarios que han hecho prestamos")
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
    
    
            
        
    
    
    






