# Se define la clase base 'Persona' con atributos personales
class Persona:
    def __init__(self, nombre, apellido, edad):
        # Constructor que inicializa los atributos nombre, apellido y edad
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrarPersona(self):
        # Devuelve una descripción textual del ciudadano
        return f"El ciudadan@ {self.nombre} {self.apellido} con {self.edad} años está asistiendo a la UEA."


# Se define la clase 'Estudiante' que hereda de 'Persona' e incluye atributos académicos
class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad, carrera, semestre_o_graduado, asignatura):
        # Constructor que inicializa los atributos de la clase base y los propios
        super().__init__(nombre, apellido, edad)  # Llama al constructor de Persona
        self.carrera = carrera
        self.semestre_o_graduado = semestre_o_graduado  # Puede ser número o la cadena "GRADUADO"
        self.asignatura = asignatura  # Número total de asignaturas

    def mostrarestudiante(self):
        # Devuelve una descripción textual del estado académico del estudiante
        return f"El estudiante {self.nombre} estudia la carrera de {self.carrera}, está en el semestre número {self.semestre_o_graduado} y cursa {self.asignatura} asignaturas."


# Se define la clase 'Verificar' que hereda de 'Estudiante' y añade lógica para evaluar el estado académico
class Verificar(Estudiante):
    def __init__(self, nombre, apellido, edad, carrera, semestre_o_graduado, asignatura):
        # Constructor que inicializa todos los atributos heredados
        super().__init__(nombre, apellido, edad, carrera, semestre_o_graduado, asignatura)

    def verificacion(self):
        # Determina el estado académico del estudiante según el valor de 'semestre_o_graduado'
        if self.semestre_o_graduado == "GRADUADO":
            return "Ya se ha graduado"
        elif self.semestre_o_graduado == 8:
            return "Muy pronto se gradúa"
        elif self.semestre_o_graduado in [1, 2, 3, 4, 5, 6, 7]:
            return "Continúa"
        else:
            return "Estudiante se ha retirado"

    def mostrar_verificacion(self):
        # Devuelve una frase que identifica al estudiante y su estado académico actual
        return f"El estudiante {self.nombre}: {self.verificacion()}"

    def __del__(self):
        #Méttodo especial que se ejecuta al eliminar la instancia
        #Imprime un mensaje confirmando la eliminación del estudiante
        mensaje = f"Estudiante {self.nombre} {self.apellido} ha sido removido del sistema\n"
        print(mensaje)
        with open("eliminados.txt", "a", encoding="utf-8") as archivo:
            archivo.write(mensaje)

# Bloque de ejecución: se crea una persona y se utiliza para instanciar un estudiante verificado
persona1 = Persona("Juana", "Quiroz", 19)  # Se instancia un objeto de la clase 'Persona'

# Se instancia un objeto de la clase 'Verificar' usando los datos de 'persona1'
alumno = Verificar(persona1.nombre, persona1.apellido, persona1.edad, "Ingeniería", "GRADUADO", 7)

# Se imprimen resultados del méttodo mostrarPersona y mostrarestudiante
print(persona1.mostrarPersona())           # Muestra la información general del ciudadano
print(alumno.mostrarestudiante())          # Muestra la información académica del estudiante
print(alumno.mostrar_verificacion())       # Muestra el estado académico actual

# Se elimina el objeto 'alumno', lo cual activa el métodoo __del__
del alumno