
class Usuario:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol

    def __del__(self):
        print(f"El usuario {self.nombre} con rol {self.rol} ha salido del sistema.")

u = Usuario("Carlos", "Administrador")