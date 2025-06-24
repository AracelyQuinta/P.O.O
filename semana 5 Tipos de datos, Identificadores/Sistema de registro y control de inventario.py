# Clase que representa a un cliente
class Cliente:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    # Muestra el nombre del cliente
    def mostrar_cliente(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")

    # Solicita si se factura a nombre del cliente o como consumidor final
    def facturar_cliente(self):
        tipo = input("¿Desea factura con sus datos o como consumidor final? (DATOS/CONSUMIDOR): ").strip().upper()
        if tipo == "DATOS":
            return f"{self.nombre} {self.apellido}"
        elif tipo == "CONSUMIDOR":
            return "Consumidor Final"
        else:
            print("Entrada no válida. Se usará 'Consumidor Final' por defecto.")
            return "Consumidor Final"

# Clase que representa un producto en el inventario
class Producto:
    def __init__(self, fecha, descripcion, cantidad, valor_unitario):
        self.fecha = fecha                        # Fecha del movimiento
        self.descripcion = descripcion            # Nombre o detalle del producto
        self.cantidad = int(cantidad)             # Unidades adquiridas
        self.valor_unitario = float(valor_unitario)  # Precio por unidad

    # Calcula el subtotal sin impuestos
    def calcular_valor_total(self):
        return self.cantidad * self.valor_unitario

# Clase que representa una factura
class Factura:
    def __init__(self, producto, iva_porcentaje, nombre_cliente):
        self.producto = producto                      # Objeto Producto
        self.iva_porcentaje = iva_porcentaje          # Porcentaje de IVA aplicado
        self.nombre_cliente = nombre_cliente          # Nombre del cliente o 'Consumidor Final'
        self.registros = []                           # Lista para almacenar detalles si hay múltiples productos

    # Calcula el valor del IVA
    def calcular_iva(self):
        return self.producto.calcular_valor_total() * (self.iva_porcentaje / 100)

    # Devuelve el total sumando IVA
    def calcular_total_con_iva(self):
        return self.producto.calcular_valor_total() + self.calcular_iva()
    # Registra los datos del producto, IVA y total a la lista
    def generar_factura(self):
        iva = self.calcular_iva()
        total = self.calcular_total_con_iva()
        self.registros.append((
            self.producto.descripcion,
            self.producto.cantidad,
            self.producto.valor_unitario,
            iva,
            total
        ))

    # Muestra la factura de forma clara y legible
    def mostrar_factura(self):
        print("\n========= FACTURA =========")
        print(f"Cliente: {self.nombre_cliente}")
        print(f"Fecha: {self.producto.fecha}")
        print(f"Producto: {self.producto.descripcion}")
        print(f"Cantidad: {self.producto.cantidad}")
        print(f"Valor Unitario: ${self.producto.valor_unitario:.2f}")
        print(f"Subtotal: ${self.producto.calcular_valor_total():.2f}")
        print(f"IVA ({self.iva_porcentaje}%): ${self.calcular_iva():.2f}")
        print(f"Total: ${self.calcular_total_con_iva():.2f}")
        print("===========================\n")

# ==================== EJEMPLO DE USO ====================
# Solicita datos del cliente
cliente =  Cliente("Ara ", " Quintanilla")
nombre_factura = cliente.facturar_cliente()

# Crea un producto (puedes cambiar los datos si quieres interactuar)
producto = Producto("2025-06-24", "Cajas de tomate", 10, 4.00)

# Genera y muestra la factura con un 12% de IVA
factura = Factura(producto, 15, nombre_factura)
factura.generar_factura()
factura.mostrar_factura()

