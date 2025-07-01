class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    # Método para mostrar los detalles del producto
    def mostrar(self):
        print(f"Código: {self.codigo} / Nombre: {self.nombre} / Precio: ${self.precio:.2f} / Stock: {self.stock}")

# Diccionario para almacenar los productos
# La clave es el código del producto y el valor es una instancia de Producto
productos = {}

# Funciones para manejar el catálogo de productos
# Agregar un nuevo producto al catálogo
def agregar_productos():
    codigo = int(input("Ingrese el código del producto: "))
    if codigo in productos:
        print("El producto ya existe.")
    else:
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese el stock del producto: "))
        productos[codigo] = Producto(codigo, nombre, precio, stock)
        print("Producto agregado exitosamente.")

# Mostrar todos los productos en el catálogo
def mostrar_productos():
    if productos:
        print("Productos: ")
        for p in productos.values():
            p.mostrar()
    else:
        print("No hay productos en el catálogo.")

# Actualizar el stock de un producto existente
# Permite sumar o restar del stock actual
def actualizar_stock():
    codigo = int(input("Ingrese el código del producto que quiere actualizar: "))
    if codigo in productos:
        opcion = input("¿Desea sumar o restar del stock? (s/r): ").lower()
        if opcion not in ['s', 'r']:
            print("Opción no válida. Debe ser 's' para sumar o 'r' para restar.")
            return
        elif opcion == 'r':
            cant = int(input("Ingrese la cantidad que quisiera restar del stock: "))
            if productos[codigo].stock < cant:
                print("No hay suficiente stock para restar esa cantidad.")
                return
            else:
                productos[codigo].stock -= cant
                print(f"Stock actualizado: {productos[codigo].stock} unidades disponibles.")
                
        elif opcion == 's':
            cant = int(input("Ingrese la cantidad que quisiera sumar al stock: "))
            productos[codigo].stock += cant
            print(f"Stock actualizado: {productos[codigo].stock} unidades disponibles.")
    else:
        print("Producto no encontrado.")

# Programa principal que permite interactuar con el catálogo de productos
# Muestra un menú y permite al usuario seleccionar opciones
def main():
    while True:
        print ("1.Agregar producto. \n2.Mostrar productos.\n3.Actualizar stock.\n4.Salir.")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_productos()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            actualizar_stock()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

main()

