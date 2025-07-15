class Vehiculo:
    def __init__(self, placa, tipo):
        self.__placa = placa       # Atributo privado
        self.__tipo = tipo         # Atributo privado
        print(f" Entrada: {self.__tipo} con placa {self.__placa} ingresó al parqueadero.")

    # Uso del metodo destructor __del__para liberar espacio
    def __del__(self):
        print(f" Salida: {self.__tipo} con placa {self.__placa} salió del parqueadero.")

    # Méttodo para mostrar detalles del vehículo
    def mostrar_detalles(self):
        print(f" Detalles del vehículo: Tipo = {self.__tipo}, Placa = {self.__placa}")

vehiculo1= Vehiculo("vjk125", "Moto")
