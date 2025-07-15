import tkinter as tk                       # Importa la librería tkinter para crear la interfaz gráfica
from tkinter import messagebox             # Importa los cuadros de diálogo para mostrar mensajes al usuario

from gestiondepacientes import Persona, Paciente, TipoDePaciente  # Importa tus clases desde otro archivo

# Clase principal que define la interfaz de la aplicación
class VentanaHospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Pacientes")  # Título de la ventana
        self.paciente = None                     # Se inicializa sin paciente registrado

        # Lista de campos que se mostrarán en la interfaz
        etiquetas = ["Nombre", "Apellido", "Edad", "Motivo", "Especialidad", "Doctor"]
        self.entradas = {}  # Diccionario para guardar los campos de entrada

        # Crea las etiquetas y entradas dinámicamente
        for i, campo in enumerate(etiquetas):
            tk.Label(root, text=campo + ":").grid(row=i, column=0, sticky="e")  # Coloca una etiqueta
            self.entradas[campo] = tk.Entry(root)                                # Crea un campo de entrada
            self.entradas[campo].grid(row=i, column=1)                           # Lo posiciona en la interfaz

        # Botón para registrar un nuevo paciente
        tk.Button(root, text="Registrar paciente", command=self.crear_paciente).grid(row=6, column=0, columnspan=2, pady=5)

        # Botón para agregar un nuevo motivo de consulta
        tk.Button(root, text="Agregar motivo", command=self.agregar_motivo).grid(row=7, column=0, columnspan=2)

        # Botón para mostrar la información del paciente registrado
        tk.Button(root, text="Mostrar información", command=self.mostrar_informacion).grid(row=8, column=0, columnspan=2, pady=5)

    # Función que crea un paciente a partir de los datos ingresados
    def crear_paciente(self):
        try:
            # Recupera los valores escritos por el usuario
            nombre = self.entradas["Nombre"].get()
            apellido = self.entradas["Apellido"].get()
            edad = int(self.entradas["Edad"].get())  # Convierte edad a entero
            motivo = self.entradas["Motivo"].get()
            especialidad = self.entradas["Especialidad"].get()
            doctor = self.entradas["Doctor"].get()

            # Crea una instancia de TipoDePaciente
            self.paciente = TipoDePaciente(nombre, apellido, edad, motivo, especialidad, doctor)
            messagebox.showinfo("Paciente registrado", f"Paciente {nombre} creado exitosamente.")
        except ValueError:
            # Si ocurre un error al convertir la edad, se muestra un mensaje
            messagebox.showerror("Error", "Edad debe ser un número entero.")

    # Función para añadir un nuevo motivo de consulta
    def agregar_motivo(self):
        if self.paciente:
            nuevo_motivo = self.entradas["Motivo"].get()
            self.paciente.insertar_motivo(nuevo_motivo)
            messagebox.showinfo("Motivo agregado", f"Nuevo motivo añadido: {nuevo_motivo}")
        else:
            messagebox.showwarning("Atención", "Primero debe registrar un paciente.")

    # Función que muestra todos los datos del paciente en un cuadro emergente
    def mostrar_informacion(self):
        if self.paciente:
            info = [
                self.paciente.mostrar_datos_de_la_persona(),
                self.paciente.mostrar_tipo(),               # Clasificación por edad
                self.paciente.mostrar_motivos(),            # Todos los motivos de consulta
                self.paciente.mostrar_asignacion()          # Doctor asignado
            ]
            # Muestra toda la información en un cuadro de mensaje
            messagebox.showinfo("Información del paciente", "\n".join(info))
        else:
            messagebox.showwarning("Atención", "No hay paciente registrado.")

# ---------- BLOQUE PRINCIPAL ----------
if __name__ == "__main__":
    root = tk.Tk()                     # Crea la ventana principal (root es la raíz de la interfaz)
    app = VentanaHospital(root)       # Se pasa root a la clase que diseña la interfaz

    # Asegura que la ventana esté al frente
    root.lift()
    root.attributes("-topmost", True)
    root.after_idle(root.attributes, "-topmost", False)

    root.mainloop()  # Inicia el bucle de eventos de Tkinter (necesario para que la app permanezca abierta)