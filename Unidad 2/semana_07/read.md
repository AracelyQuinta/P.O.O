# Este programa define un sistema de clases orientado a representar personas y estudiantes en contexto universitario, con verificación de su estado académico.
## Estructura y propósito:
- Persona: Clase base que almacena información básica como nombre, apellido y edad. Incluye el método mostrarPersona() para presentar esta información.
- Estudiante: Clase derivada que añade atributos académicos: carrera, semestre o estado ("GRADUADO"), y número de asignaturas. Su método mostrarestudiante() describe esos datos académicos.
- Verificar: Clase que hereda de Estudiante y añade una lógica de evaluación para saber si el estudiante continúa sus estudios, está por graduarse, ya se ha graduado o se ha retirado. También implementa __del__, el método especial que se ejecuta al eliminar una instancia de esta clase, imprimiendo una notificación.
## Modo de ejecución:
- Se crea una instancia de Persona con los datos de un ciudadano.
- Se usa esa información para crear un estudiante.
- Se muestran en pantalla:
- La información personal del ciudadano.
- Su información académica.
- El resultado de la evaluación académica.
- Finalmente, se elimina explícitamente el estudiante mediante del.
![image](https://github.com/user-attachments/assets/f52e8945-67cf-4fe8-8a91-fe83d06a5e52)
