# Programación Tradicional
# Ejemplo: Determinacion del promedio semanal del clima.

def calculo_de_la_temperatura_semanal():
    temperaturas = []  # Lista para almacenar temperaturas de cada día

    dias_de_la_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    for i in range(7):
        dia = input(f"Inserta el día ({dias_de_la_semana[i]}): ")

        # Validar si el día ingresado es correcto
        if dia not in dias_de_la_semana:
            return f"El día '{dia}' no se encuentra en los datos."

        else:
            temperatura = float(input(f"Inserta la temperatura de {dia}: "))
            temperaturas.append(temperatura)  # Guardamos la temperatura

    # Calcular promedio semanal
    promedio = sum(temperaturas) / len(temperaturas)
    print(f"La temperatura promedio semanal es: {promedio:.2f}°C")


calculo_de_la_temperatura_semanal()  # Llamada a la función
