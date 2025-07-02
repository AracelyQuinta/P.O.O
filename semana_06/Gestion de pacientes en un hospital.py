"""
 Gestión de Pacientes en un Hospital
"""# Clase base que define atributos generales de cualquier persona
class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre                     # Nombre del paciente
        self.apellido = apellido                 # Apellido del paciente
        self.edad = edad                         # Edad del paciente

    def mostrar_datos_de_la_persona(self):
        return f"Se llama {self.nombre} {self.apellido} y tiene {self.edad} años."


# Clase que hereda de Persona y representa a un paciente con información médica adicional
class Paciente(Persona):
    def __init__(self, nombre, apellido, edad, motivo_de_consulta, especialidad_del_doctor, doctor_asignado):
        super().__init__(nombre, apellido, edad)         # Hereda nombre, apellido y edad
        self.__motivo_de_consulta = [motivo_de_consulta] # Motivos encapsulados como lista privada
        self.especialidad_del_doctor = especialidad_del_doctor  # Especialidad médica asignada
        self.doctor_asignado = doctor_asignado                  # Nombre del médico

    # Polimorfismo: método sobrescrito para presentarse como paciente
    def mostrar_datos_de_la_persona(self):
        return f"El paciente se llama {self.nombre} {self.apellido} y tiene {self.edad} años."

    # Método para agregar un nuevo motivo de consulta
    def insertar_motivo_de_la_consulta(self, nuevo_motivo):
        self.__motivo_de_consulta.append(nuevo_motivo)

    # Devuelve todos los motivos en una cadena separada por comas
    def mostrar_motivo_de_la_consulta(self):
        return f"Motivo(s) de consulta: {', '.join(self.__motivo_de_consulta)}"

    # Muestra el nombre del especialista asignado y su especialidad
    def mostrar_asignacion(self):
        return f"Se ha asignado al Dr. {self.doctor_asignado}, especialista en {self.especialidad_del_doctor}."


# Clase que extiende Paciente para incluir clasificación automática según edad
class TipoDePaciente(Paciente):
    def __init__(self, nombre, apellido, edad, motivo, especialidad, doctor):
        super().__init__(nombre, apellido, edad, motivo, especialidad, doctor)  # Llama al constructor del padre
        self.tipo_de_paciente = self.clasificar_por_edad()  # Calcula tipo automáticamente

    # Método que clasifica al paciente en una categoría según la edad
    def clasificar_por_edad(self):
        if self.edad < 1:
            return "Recién nacido"
        elif self.edad < 3:
            return "Bebé"
        elif self.edad < 11:
            return "Niño"
        elif self.edad < 18:
            return "Adolescente"
        elif self.edad < 59:
            return "Adulto"
        else:
            return "Adulto mayor"

    # Muestra la categoría de paciente en forma legible
    def mostrar_tipo_de_paciente(self):
        return f"Tipo de paciente: {self.tipo_de_paciente}"


# Bloque principal para pruebas (se ejecuta solo si el archivo se corre directamente)
if __name__ == "__main__":
    # Se crea un paciente de prueba con todos los datos
    paciente = TipoDePaciente("Yelae", "Quiroz", 50, "Chequeo anual", "Medicina interna", "Ana Portero")

    # Se muestran todos los datos relacionados con la persona y su atención médica
    print(paciente.mostrar_datos_de_la_persona())           # Datos generales del paciente
    print(paciente.mostrar_tipo_de_paciente())              # Clasificación por edad
    print(paciente.mostrar_motivo_de_la_consulta())         # Primer motivo
    print(paciente.mostrar_asignacion())                    # Información del doctor

    # Se agrega un segundo motivo de consulta
    paciente.insertar_motivo_de_la_consulta("Dolor de cabeza")
    print(paciente.mostrar_motivo_de_la_consulta())         # Se muestran ambos motivos