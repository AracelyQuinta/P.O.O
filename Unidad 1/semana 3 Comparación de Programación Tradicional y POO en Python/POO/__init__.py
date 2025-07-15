#POO
# Definimos la clase Climapordia para almacenar la información de un día específico
class Climapordia:
    def __init__(self, dia, temperatura):
        """Inicializa un objeto con el día y la temperatura correspondiente."""
        self.dia = dia  # Guarda el nombre del día (Ejemplo: "Lunes")
        self.temperatura = temperatura  # Guarda la temperatura registrada (Ejemplo: 23.5°C)

    def mostrar(self):
        """Muestra el día y su temperatura almacenada en formato legible."""
        print(f"{self.dia}: {self.temperatura}°C")  # Se formatea con dos decimales para mejor presentación


# Definimos la clase SemanaClima que gestionará los datos de la semana
class SemanaClima:
    def __init__(self):
        """Inicializa una lista vacía donde se almacenarán los datos de cada día."""
        self.registro = []  # Lista para almacenar objetos Climapordia

    def agregar_dia(self, dia, temperatura):
        """Añade un día con su temperatura a la lista de registros."""
        self.registro.append(Climapordia(dia, temperatura))  # Se crea un objeto Climapordia y se añade a la lista

    def mostrar_semana(self):
        """Muestra todas las temperaturas registradas en la semana."""
        print("\nRegistro semanal de temperaturas:")
        for clima in self.registro:  # Iteramos sobre la lista de objetos Climapordia
            clima.mostrar()  # Se llama al método mostrar() de cada objeto

    def promedio(self):
        """Calcula el promedio de las temperaturas registradas en la semana."""
        if len(self.registro) == 0:  # Verifica si hay datos almacenados antes de calcular el promedio
            print("No hay temperaturas registradas.")  # Mensaje de advertencia si no hay datos
            return
        
        # Extrae las temperaturas de cada objeto Climapordia en la lista
        promedio1 = sum([clima.temperatura for clima in self.registro]) / len(self.registro)
        
        # Imprime el resultado con dos decimales de precisión
        print(f"La temperatura promedio de la semana es: {promedio1:.2f}°C")


# Se crea una instancia de SemanaClima para almacenar los datos
semana = SemanaClima()

# Lista con los nombres de los días de la semana
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Bucle para pedir la temperatura de cada día y almacenarla en la instancia de SemanaClima
for dia in dias_semana:
    tempe = float(input(f"Digite la temperatura de {dia}: "))  # Se solicita y convierte la entrada a tipo flotante
    semana.agregar_dia(dia, tempe)  # Se almacena la temperatura ingresada

# Se muestra el registro completo de temperaturas
semana.mostrar_semana()

# Se calcula el promedio de las temperaturas registradas en la semana
semana.promedio()
