import os  # Importa el módulo para manejar rutas y directorios
import subprocess  # Permite ejecutar comandos del sistema operativo

# Función que muestra el contenido de un script Python
def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)  # Convierte la ruta en absoluta para localizar correctamente el archivo
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()  #
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None

# Función para ejecutar el script seleccionado
def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])  # Usa xterm para ejecutar y mantener abierta la terminal
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")

# Función principal que muestra el menú inicial
def mostrar_menu():
    ruta_base = os.path.dirname(__file__)  # Obtiene la ruta del archivo actual

    unidades = {  # Diccionario con las unidades disponibles
        '1': 'Unidad 1',
        '2': 'Unidad 2',
        '3': 'Clase',
    }

    while True:  # Bucle para mantener el menú activo
        print("\nMenu Principal - Dashboard")
        for key in unidades:
            print(f"{key} - {unidades[key]}")
        print("0 - Salir")

        eleccion_unidad = input("Elige una unidad o '0' para salir: ")
        if eleccion_unidad == '0':
            print("Saliendo del programa.")
            break
        elif eleccion_unidad in unidades:  # Si la elección está en el diccionario
            mostrar_sub_menu(os.path.join(ruta_base, unidades[eleccion_unidad]))  # Llama al submenú correspondiente
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")  # Si la opción no es válida

# Función que muestra las subcarpetas de la unidad el3egida
def mostrar_sub_menu(ruta_unidad):
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]  # Lista todas las carpetas dentro de la unidad

    while True:
        print("\nSubmenú - Selecciona una subcarpeta")
        for i, carpeta in enumerate(sub_carpetas, start=1):  # Muestra las carpetas numeradas
            print(f"{i} - {carpeta}")
        print("0 - Regresar al menú principal")

        eleccion_carpeta = input("Elige una subcarpeta o '0' para regresar: ")
        if eleccion_carpeta == '0':
            break
        else:
            try:
                eleccion_carpeta = int(eleccion_carpeta) - 1  # Convierte la elección en índice
                if 0 <= eleccion_carpeta < len(sub_carpetas):
                    mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[eleccion_carpeta]))
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")  # Si el índice está fuera de rango
            except ValueError:  # Si la entrada no es un número
                print("Opción no válida. Por favor, intenta de nuevo.")

# Función que muestra y permite ejecutar los scripts en una subcarpeta
def mostrar_scripts(ruta_sub_carpeta):
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]  # Filtra archivos .py

    while True:
        print("\nScripts - Selecciona un script para ver y ejecutar")
        for i, script in enumerate(scripts, start=1):  # Muestra los scripts disponibles
            print(f"{i} - {script}")
        print("0 - Regresar al submenú anterior")
        print("5 - Regresar al menú principal")

        eleccion_script = input("Elige un script, '0' para regresar o '9' para ir al menú principal: ")  # Entrada del usuario
        if eleccion_script == '0':  # Regresa al submenú
            break
        elif eleccion_script == '5':  # Regresa al menú principal
            return
        else:
            try:
                eleccion_script = int(eleccion_script) - 1  # Convierte la entrada en índice
                if 0 <= eleccion_script < len(scripts):  # Verifica que el índice sea válido
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[eleccion_script])  # Construye la ruta completa al script
                    codigo = mostrar_codigo(ruta_script)
                    if codigo:
                        ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                        elif ejecutar == '0':
                            print("No se ejecutó el script.")
                        else:
                            print("Opción no válida. Regresando al menú de scripts.")
                        input("\nPresiona Enter para volver al menú de scripts.")
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Por favor, intenta de nuevo.")

# Punto de entrada del programa, ejecuta el menú principal
if __name__ == "__main__":     #Verifica si el script se ejecuta directamente y llama a la función principal del menú.
    mostrar_menu()