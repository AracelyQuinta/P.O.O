# Programación Orientada a Objetos (POO)
# Sistema simple de reservas de habitaciones de hotel

# Se define la clase que representa una habitación del hotel
class Habitacion:
    def __init__(self, numero, tipo, precio_por_hora, disponible=True):
        self.numero = numero              # Número único de la habitación
        self.tipo = tipo                  # Tipo de habitación (ej: sauna, vip, etc.)
        self.precio_por_hora = precio_por_hora  # Precio que se cobra por hora
        self.disponible = disponible      # Estado: True si está libre, False si está ocupada

    def mostrar_info(self):
        estado = "Disponible" if self.disponible else "No disponible"  # Determina si la habitación está libre o no
        return f"Habitación {self.numero} - Tipo: {self.tipo} - Precio/hora: ${self.precio_por_hora} - {estado}"  # Muestra los datos

    def reservar(self, horas):
        if self.disponible:                     # Verifica si está disponible
            self.disponible = False             # Cambia el estado a ocupada
            total = self.precio_por_hora * horas  # Calcula el costo total por las horas reservadas
            return f"Reserva confirmada. Total a pagar por {horas} horas: ${total}"  # Mensaje de confirmación
        else:
            return " Lo siento, esta habitación no está disponible."  # Mensaje si ya está ocupada

# Clase que gestiona todas las habitaciones del hotel
class Hoteleria:
    def __init__(self):
        self.habitaciones = []  # Lista donde se almacenan todas las habitaciones

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)  # Añade una habitación al listado

    def mostrar_habitaciones(self):
        return [hab.mostrar_info() for hab in self.habitaciones]  # Muestra info de todas las habitaciones

    def buscar_habitacion(self, numero):
        for hab in self.habitaciones:  # Recorre cada habitación
            if hab.numero == numero:   # Compara el número con el que busca el usuario
                return hab             # Si la encuentra, la retorna
        return None                    # Si no está, devuelve None

    def reservar_habitacion(self, numero, horas):
        habitacion = self.buscar_habitacion(numero)  # Busca la habitación
        if habitacion:                               # Si existe...
            return habitacion.reservar(horas)        # ...intenta reservarla
        else:
            return " Habitación no encontrada."      # Mensaje si no existe

# Zona principal del programa, donde se ejecuta todo
hotel = Hoteleria()  # Crea un objeto hotel con su lista de habitaciones vacía

# Se agregan cuatro habitaciones con diferentes características
hotel.agregar_habitacion(Habitacion(101, "sauna", 40))
hotel.agregar_habitacion(Habitacion(102, "vip", 30))
hotel.agregar_habitacion(Habitacion(103, "normal", 20))
hotel.agregar_habitacion(Habitacion(104, "económico", 15))

# Se imprime el estado actual de cada habitación del hotel
print(" Estado actual de las habitaciones:")
for info in hotel.mostrar_habitaciones():  # Recorre cada habitación y la imprime
    print(info)

# Se solicita al usuario que ingrese los datos para hacer una reserva

entrada_numero = input("\nIngrese el número de habitación que desea reservar: ")  # Se guarda el número ingresado

if entrada_numero.isdigit():                     # Se valida que sea un número
    numero = int(entrada_numero)                 # Se convierte a entero

    entrada_horas = input("Ingrese el número de horas que desea reservar: ")  # Pide las horas
    if entrada_horas.isdigit():                  # Valida que también sea un número
        horas = int(entrada_horas)               # Se convierte a entero

        print("\n" + hotel.reservar_habitacion(numero, horas))  # Intenta reservar y muestra el resultado
    else:
        print("Debe ingresar un número válido para las horas.")  # Mensaje de error si no es número
else:
    print("Debe ingresar un número válido para la habitación.")  # Mensaje de error si no es número