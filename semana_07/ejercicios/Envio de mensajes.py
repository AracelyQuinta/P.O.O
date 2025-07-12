# Clase Usuario: representa a una persona en el sistema
class Usuario:
    def __init__(self):
        self.nombre = input("Ingrese el nombre del usuario: ")
        self.tipo = input("Ingrese el tipo de usuario (Ej. Estudiante, Médico, etc.): ")
        print(f"Usuario creado: {self.nombre}, tipo: {self.tipo}")

    def __del__(self):
        print(f"El usuario {self.nombre} ha salido.")

# Clase Mensaje: gestiona la información del mensaje y contiene al usuario como atributo
class Mensaje:
    def __init__(self):
        self.usuario = Usuario()  # Se crea automáticamente el usuario al crear el mensaje
        self.motivo = ""
        self.contenido = ""
        print("Mensaje preparado para envío.")

    def mostrar(self):
        self.motivo = input("Ingrese el motivo o asunto: ")

    def mostrarcontenido(self):
        self.contenido = input("Detalle su mensaje: ")

    def guardar(self):
        mensaje = f"Usuario: {self.usuario.nombre} - Motivo: {self.motivo} - Contenido: {self.contenido}\n"
        with open("Mensajes guardados.txt", "a", encoding="utf-8") as archivo:
            archivo.write(mensaje)
        print("Mensaje guardado correctamente.")

# Bloque principal automático y sencillo
mensaje1 = Mensaje()
mensaje1.mostrar()
mensaje1.mostrarcontenido()
mensaje1.guardar()

# Liberación de memoria (opcional)
