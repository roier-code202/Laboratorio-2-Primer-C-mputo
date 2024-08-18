class Auto:
    def __init__(self, marca, modelo, anio, color, precio_compra, tipo):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color
        self.precio_compra = precio_compra
        self.tipo = tipo  # Nacional o Importado
        self.precio_venta = self.calcular_precio_venta()

    def calcular_precio_venta(self):
        return self.precio_compra * 1.4

    def mostrar_informacion(self):
        return (f'Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}, '
                f'Color: {self.color}, Tipo: {self.tipo}, '
                f'Precio Compra: {self.precio_compra:.2f}, Precio Venta: {self.precio_venta:.2f} USD')


class AutoNacional(Auto):
    def __init__(self, marca, modelo, anio, color, precio_compra):
        super().__init__(marca, modelo, anio, color, precio_compra, "Nacional")


class AutoImportado(Auto):
    def __init__(self, marca, modelo, anio, color, precio_compra):
        super().__init__(marca, modelo, anio, color, precio_compra, "Importado")


def main():
    lista_autos = []

    for _ in range(2):  # Permitir registrar 2 autos
        print("\nRegistro de Auto")
        tipo = input("Ingrese el tipo de vehiculo (Nacional/Importado): ").strip().lower()
        
        # Validar tipo
        if tipo not in ['nacional', 'importado']:
            print("Tipo de vehiculo inválido. Debe ser 'Nacional' o 'Importado'.")
            continue
        
        marca = input("Ingrese la marca del vehiculo: ")
        modelo = input("Ingrese el modelo del vehiculo: ")
        anio = int(input("Ingrese el año del vehiculo: "))
        color = input("Ingrese el color del vehiculo: ")
        precio_compra = float(input("Ingrese el precio de compra del vehiculo: "))
        
        # Crear instancia de Auto según el tipo
        if tipo == 'nacional':
            auto = AutoNacional(marca, modelo, anio, color, precio_compra)
        else:
            auto = AutoImportado(marca, modelo, anio, color, precio_compra)
        
        # Agregar a la lista de autos
        lista_autos.append(auto)
        print(f"\nAuto registrado: {auto.mostrar_informacion()}")

    print("\n Los vehiculos han sido registrados con éxito.")


if __name__ == "__main__":
    main()