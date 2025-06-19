# Programación Orientada a Objetos (POO)
# Ejemplo: Sistemas de Reservas de hoteles


class Hoteleria:
    def __init__(self,numero_de_habitacion, tipo_de_habitacion,disponibilidad,precio_de_la_habitacion):
        self.numero_de_habitacion = numero_de_habitacion
        self.tipo_de_habitacion = tipo_de_habitacion
        self.disponibilidad = disponibilidad
        self.precio_de_la_habitacion = precio_de_la_habitacion

