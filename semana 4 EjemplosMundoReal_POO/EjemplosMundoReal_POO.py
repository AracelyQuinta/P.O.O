# Programación Orientada a Objetos (POO)
# Sistema simple de reservas de habitaciones de hotel

# Clase que representa una habitación
class Habitacion:
    def __init__(self, numero, tipo, precio_por_hora, disponible=True):
        # Inicializa los atributos de la habitación
        self.numero = numero
        self.tipo = tipo
        self.precio_por_hora = precio_por_hora
        self.disponible = disponible

    def mostrar_info(self):
        # Muestra la información detallada de la habitación
        estado = "Disponible" if self.disponible else "No disponible"
        return f"Habitación {self.numero} - Tipo: {self.tipo} - Precio/hora: ${self.precio_por_hora} - {estado}"

    def reservar(self, horas):
        # Permite reservar la habitación si está disponible
        if self.disponible:
            self.disponible = False
            total = self.precio_por_hora * horas
            return f"Reserva confirmada. Total a pagar por {horas} horas: ${total}"
        else:
            return " Lo siento, esta habitación no está disponible."

# Clase que gestiona todas las habitaciones del hotel
class Hoteleria:
    def __init__(self):
        # Lista vacía para almacenar las habitaciones
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        # Agrega una nueva habitación al hotel
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones(self):
        # Muestra todas las habitaciones con su estado
        return [hab.mostrar_info() for hab in self.habitaciones]

    def buscar_habitacion(self, numero):
        # Busca una habitación por su número
        for hab in self.habitaciones:
            if hab.numero == numero:
                return hab
        return None

    def reservar_habitacion(self, numero, horas):
        # Realiza la reserva si la habitación existe
        habitacion = self.buscar_habitacion(numero)
        if habitacion:
            return habitacion.reservar(horas)
        else:
            return " Habitación no encontrada."

# Zona principal del programa
# Crear una instancia de hotel
hotel = Hoteleria()

# Agregar habitaciones al sistema
hotel.agregar_habitacion(Habitacion(101, "sauna", 40))
hotel.agregar_habitacion(Habitacion(102, "vip", 30))
hotel.agregar_habitacion(Habitacion(103, "normal", 20))
hotel.agregar_habitacion(Habitacion(104, "económico", 15))

# Mostrar el estado actual de todas las habitaciones
print(" Estado actual de las habitaciones:")
for info in hotel.mostrar_habitaciones():
    print(info)

# Solicitar número de habitación y horas al usuario, validando entrada sin try/except
entrada_numero = input("\nIngrese el número de habitación que desea reservar: ")
if entrada_numero.isdigit():
    numero = int(entrada_numero)

    entrada_horas = input("Ingrese el número de horas que desea reservar: ")
    if entrada_horas.isdigit():
        horas = int(entrada_horas)
        # Ejecutar la reserva y mostrar resultado
        print("\n" + hotel.reservar_habitacion(numero, horas))
    else:
        print("Debe ingresar un número válido para las horas.")
else:
    print("Debe ingresar un número válido para la habitación.")