#Funcion verificación inicio de sesion
def inicioSesion(usuarios, contrasenas):
    intentos = 0
    while intentos < 4:
        print("")
        usuario = input("Ingrese su nombre de usuario: ")
        contrasena = input("Ingrese su contraseña: ")
        acceso = False
        for i in range(len(usuarios)):
            if usuarios[i] == usuario and contrasenas[i] == contrasena:
                acceso = True
        if acceso:
            print("")
            print("✅ ---Bienvenido: ", usuario,"---")
            print("")
            return True
        else:
            print("")
            print("❌ ---DATOS INCORRECTOS---")
            print("Intentos restantes:", 3 - intentos)
            intentos += 1
    return False

def agregarProducto():
    print("")
    print("--- MENU REGISTRO DE PRODUCTOS ---")
    nProductos = int(input("Ingrese el numero de productos a registrar: "))
    i = 1
    while i > nProductos:
        print("--- PRODUCTO ", i, " ---")
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese la cantidad en stock: "))
        print("")
        i = 1

def modificarProducto():
    print("--- MODIFICAR PRODUCTO ---")

def realizarCompra():
    print("--- REALIZAR COMPRA ---")

def reporteProductos():
    print("--- REPORTE DE PRODUCTOS ---")