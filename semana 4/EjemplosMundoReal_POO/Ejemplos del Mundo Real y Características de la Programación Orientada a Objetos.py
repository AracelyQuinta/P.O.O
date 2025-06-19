# Programación Orientada a Objetos (POO)
# Ejemplo: Sistemas de Reservas de hoteles
class Habitacion:
    def __init__(self, numero, tipo, precio_por_hora, disponible=True):
        self.numero = numero
        self.tipo = tipo
        self.precio_por_hora = precio_por_hora
        self.disponible = disponible

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


#  Zona de interacción con el usuario
hotel = Hoteleria()
# Agregamos algunas habitaciones
hotel.agregar_habitacion(Habitacion(101, "sauna", 40))
hotel.agregar_habitacion(Habitacion(102, "vip", 30))
hotel.agregar_habitacion(Habitacion(103, "normal", 20))
hotel.agregar_habitacion(Habitacion(104, "económico", 15))

# Mostramos las habitaciones disponibles o no
print(" Estado actual de las habitaciones:")
for info in hotel.mostrar_habitaciones():
    print(info)

# Solicitar datos al usuario
try:
    numero = int(input("\n Ingrese el número de habitación que desea reservar: "))
    horas = int(input("Ingrese el número de horas que desea reservar: "))
    print("\n" + hotel.reservar_habitacion(numero, horas))
except ValueError:
    print(" Por favor, ingrese un número válido.")
