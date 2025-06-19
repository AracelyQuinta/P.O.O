
# Programación Orientada a Objetos (POO)
# Ejemplo: Sistemas de Reservas de hoteles


class Hoteleria:
    def __init__(self, hotel,numero_de_habitacion, tipo_de_habitacion,disponibilidad,precio_de_la_habitacion):
        self.numero_de_habitacion = numero_de_habitacion
        self.tipo_de_habitacion = tipo_de_habitacion
        self.disponibilidad = disponibilidad
        self.precio_de_la_habitacion = precio_de_la_habitacion

    def mostrar_info(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"Habitación {self.numero} - Tipo: {self.tipo} - Precio/hora: ${self.precio_por_hora} - {estado}"

    def reservar(self, horas):
        if self.disponible:
            self.disponible = False
            total = self.precio_por_hora * horas
            return f"Reserva confirmada. Total a pagar por {horas} horas: ${total}"
        else:
            return " Lo siento, esta habitación no está disponible."

class Hoteleria:
    def __init__(self):
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones(self):
        return [hab.mostrar_info() for hab in self.habitaciones]

    def buscar_habitacion(self, numero):
        for hab in self.habitaciones:
            if hab.numero == numero:
                return hab
        return None

    def reservar_habitacion(self, numero, horas):
        habitacion = self.buscar_habitacion(numero)
        if habitacion:
            return habitacion.reservar(horas)
        else:
            return " Habitación no encontrada."

    hotel = Hoteleria()

    # Agrega 4 habitaciones al hotel
    hotel.agregar_habitacion(Habitacion(101, "sauna", 40))
    hotel.agregar_habitacion(Habitacion(102, "vip", 30))
    hotel.agregar_habitacion(Habitacion(103, "normal", 20))
    hotel.agregar_habitacion(Habitacion(104, "económico", 15))

    # Muestra el estado actual
    print(" Estado actual de las habitaciones:")
    for info in hotel.mostrar_habitaciones():
        print(info)