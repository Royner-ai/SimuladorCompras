import Function

#Contraseñas y usuarios precargados
usuarios = ["davirosas", "admin", "cliente"]
contrasenas = ["davirosas123","admin123", "cliente123"]

#Listas de productos
productos = []
precios = []
stocks = []

#Verificación usuario inicio de sesión
print("")
print("---Bienvenido a BigStore---")
acceso = Function.inicioSesion(usuarios, contrasenas)

#Main - Menu y flujo principal del sistema
if acceso==True:
    op = 0
    while op != 5:
        print("")
        print("--- 🏠 MENÚ BIGSTORE ---")
        print("1 - Agregar productos")
        print("2 - Modificar producto")
        print("3 - Realizar compra")
        print("4 - Reporte de productos")
        print("5 - Salir del programa")
        print("")
        op = int(input("Ingrese el número de la opción deseada: "))

        #Funciones del menu
        if op == 1:
            Function.agregarProducto(productos)
        elif op == 2:
            Function.modificarProducto(productos)
        elif op == 3:
            Function.realizarCompra(productos)
        elif op == 4:
            Function.reporteProductos(productos)
        elif op == 5:
            print("")
            print("👋 Gracias por utilizar BigStore")
            break 
        else:
            print("🚫 -Ingrese una opción valida")

elif acceso==False:
    print("")
    print("🚫 ---ACCESO DENEGADO--- 🚫")
    print("👋 Gracias por utilizar BigStore")
    break
else:
    print("")
    print("👋 Gracias por utilizar BigStore")
    break 
