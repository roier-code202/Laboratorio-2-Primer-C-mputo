class DispositivoElectronico:
    def __init__(self, marca, modelo, anio, color, precio_compra, caracteristicas):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color
        self.precio_compra = precio_compra
        self.caracteristicas = caracteristicas  # Lista de las características
        self.precio_venta = self.calcular_precio_venta()

    def calcular_precio_venta(self):
        return self.precio_compra * 1.7

    def mostrar_informacion(self):
        caracteristicas_str = ", ".join(self.caracteristicas)
        return (f'Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}, '
                f'Color: {self.color}, Características: [{caracteristicas_str}], '
                f'Precio Compra: {self.precio_compra:.2f}, Precio Venta: {self.precio_venta:.2f} USD')


class Celular(DispositivoElectronico):
    def __init__(self, modelo, anio, color, precio_compra, caracteristicas):
        super().__init__("PHR", modelo, anio, color, precio_compra, caracteristicas)


class Tablet(DispositivoElectronico):
    def __init__(self, modelo, anio, color, precio_compra, caracteristicas):
        super().__init__("PHR", modelo, anio, color, precio_compra, caracteristicas)


class Portatil(DispositivoElectronico):
    def __init__(self, modelo, anio, color, precio_compra, caracteristicas):
        super().__init__("PHR", modelo, anio, color, precio_compra, caracteristicas)


def main():
    lista_dispositivos = []

    # Registro de dispositivos
    for _ in range(2):  # Permitir registrar 2 dispositivos
        print("\nRegistro de Dispositivos Electrónicos")
        tipo = input("Ingrese el tipo de dispositivo (Celular/Tablet/Portatil): ").strip().lower()
        
        if tipo not in ['celular', 'tablet', 'portatil']:
            print("Tipo de dispositivo inválido. Debe de ser 'Celular', 'Tablet' o 'Portatil'.")
            continue
        
        modelo = input("Ingrese el modelo del dispositivo: ")
        anio = int(input("Ingrese el año del dispositivo: "))
        color = input("Ingrese el color del dispositivo: ")
        precio_compra = float(input("Ingrese el precio de compra del dispositivo: "))
        
        caracteristicas = []
        print("Debe ingresar las 6 principales características del dispositivo:")
        for i in range(6):
            caracteristica = input(f"Característica {i + 1}: ")
            caracteristicas.append(caracteristica)

        # Crear instancia de Dispositivo según el tipo
        if tipo == 'celular':
            dispositivo = Celular(modelo, anio, color, precio_compra, caracteristicas)
        elif tipo == 'tablet':
            dispositivo = Tablet(modelo, anio, color, precio_compra, caracteristicas)
        else:
            dispositivo = Portatil(modelo, anio, color, precio_compra, caracteristicas)
        
        # Agregar a la lista de dispositivos
        lista_dispositivos.append(dispositivo)
        print(f"\nDispositivo registrado: {dispositivo.mostrar_informacion()}")
    
    print("\n Los dispositivos han sido registrados con éxito.")


if __name__ == "__main__":
    main()