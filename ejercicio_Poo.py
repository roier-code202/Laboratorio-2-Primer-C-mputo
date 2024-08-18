#Este programa proporciona una solución para la gestión del inventario de una ferreteria. 
#Permite a los empleados llevar un control adecuado de las herramientas disponibles, 
#El cual facilita la adición de nuevos artículos y la consulta de la información existente.
#De esta manera,se mejora la gestión de los recursos de la tienda y se optimiza el servicio al cliente, 
# Ahora los empleados pueden acceder rápidamente a los detalles de las herramientas en stock.

class Herramienta:
    def __init__(self, nombre, categoria, marca, modelo, precio_compra, cantidad):
        self.nombre = nombre
        self.categoria = categoria
        self.marca = marca
        self.modelo = modelo
        self.precio_compra = precio_compra
        self.cantidad = cantidad

    def mostrar_informacion(self):
        return (f'Nombre: {self.nombre}, Categoría: {self.categoria}, '
                f'Marca: {self.marca}, Modelo: {self.modelo}, '
                f'Precio de Compra: {self.precio_compra:.2f}, '
                f'Cantidad en Stock: {self.cantidad}')


class Inventario:
    def __init__(self):
        self.herramientas = []

    def agregar_herramienta(self):
        print("\nRegistro de una nueva herramienta")
        nombre = input("Ingresa el nombre de la herramienta: ")
        categoria = input("Ingresa la categoría de la herramienta: ")
        marca = input("Ingresa la marca de la herramienta: ")
        modelo = input("Ingresa el modelo de la herramienta: ")
        precio_compra = float(input("Ingresa el precio de compra de la herramienta: "))
        cantidad = int(input("Ingresa la cantidad disponible en stock: "))
        
        herramienta = Herramienta(nombre, categoria, marca, modelo, precio_compra, cantidad)
        self.herramientas.append(herramienta)
        print("Herramienta registrada con éxito.")

    def consultar_herramientas(self):
        if not self.herramientas:
            print("No hay herramientas registradas en el inventario.")
            return
        print("\nLista de herramientas registradas:")
        for herramienta in self.herramientas:
            print(herramienta.mostrar_informacion())


def main():
    inventario = Inventario()

    while True:
        print("\n--- Menú de Inventario de Herramientas ---")
        print("1. Agregar herramienta")
        print("2. Consultar herramientas")
        print("3. Salir")
        opcion = input("Elige una opción (1-3): ")

        if opcion == '1':
            inventario.agregar_herramienta()
        elif opcion == '2':
            inventario.consultar_herramientas()
        elif opcion == '3':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elige una opción válida.")


if __name__ == "__main__":
    main()
