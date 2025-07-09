# Clase Usuario: representa a una persona en el sistema
class Usuario:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        print(f"Usuario creado: {self.nombre}, tipo: {self.tipo}")

    def __del__(self):
        print(f"El usuario {self.nombre} ha salido.")

# Clase Mensaje: hereda de Usuario y gestiona la información de los mensajes
class Mensaje(Usuario):
    def __init__(self, nombre, tipo, motivo="", contenido=""):
        super().__init__(nombre, tipo)
        self.motivo = motivo
        self.contenido = contenido
        print("Mensaje preparado para envío.")

    def mostrar(self):
        self.motivo = input("Ingrese el motivo o asunto: ")

    def mostrarcontenido(self):
        self.contenido = input("Detalle su mensaje: ")

    def guardar(self):
        mensaje = f"Usuario: {self.nombre} - Motivo: {self.motivo} - Contenido: {self.contenido}\n"
        with open("Mensajes guardados.txt", "a", encoding="utf-8") as archivo:
            archivo.write(mensaje)
        print("Mensaje guardado correctamente.")

# Bloque principal de ejecución
mensaje1 = Mensaje("Juana", "Estudiante")  # El mensaje ya crea y representa al usuario
mensaje1.mostrar()
mensaje1.mostrarcontenido()
mensaje1.guardar()

# Liberar memoria (opcional en Python, pero lo incluimos por claridad del ciclo de vida)
del mensaje1