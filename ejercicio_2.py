class Articulo:
    def __init__(self, nombre, precio_compra):
        self.nombre = nombre
        self.precio_compra = precio_compra
        self.precio_venta = self.calcular_precio_venta()

    def calcular_precio_venta(self):
        return self.precio_compra * 1.30


class Cuaderno(Articulo):
    def __init__(self, cantidad_hojas, precio_compra):
        nombre = "Cuaderno " + str(cantidad_hojas) + " hojas - Marca: HOJITAS"
        super().__init__(nombre, precio_compra)
        self.cantidad_hojas = cantidad_hojas


class Lapiz(Articulo):
    def __init__(self, tipo, precio_compra):
        nombre = tipo + " - Marca: RAYADO"
        super().__init__(nombre, precio_compra)
        self.tipo = tipo


def main():
    lista_articulos = []

    # Registro de cuadernos
    for _ in range(2):  # Permitir registrar 2 cuadernos
        print("\nRegistro de Cuaderno")
        cantidad_hojas = int(input("Ingrese la cantidad de hojas (50 o 100): "))
        precio_compra = float(input("Ingrese el precio de compra del cuaderno: "))
        
        cuaderno = Cuaderno(cantidad_hojas, precio_compra)
        lista_articulos.append(cuaderno)
        print(f"\nCuaderno registrado: {cuaderno.nombre}, Precio de venta: {cuaderno.precio_venta:.2f} USD")

    # Registro de lápices
    for _ in range(2):  # Permitir registrar 2 lápices
        print("\nRegistro de Lápiz")
        tipo = input("Ingrese el tipo de lápiz (Grafito o Colores): ")
        precio_compra = float(input("Ingrese el precio de compra del lápiz: "))
        
        lapiz = Lapiz(tipo, precio_compra)
        lista_articulos.append(lapiz)
        print(f"\nLápiz registrado: {lapiz.nombre}, Precio de venta: {lapiz.precio_venta:.2f} USD")

    print("\n Los artículos han sidos registrados con éxito.")


if __name__ == "__main__":
    main()