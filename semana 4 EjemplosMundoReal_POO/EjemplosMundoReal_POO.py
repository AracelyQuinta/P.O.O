
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