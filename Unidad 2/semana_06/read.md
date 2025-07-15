Este programa permite registrar pacientes con sus datos personales, asignarles médicos especialistas, almacenar múltiples motivos de consulta y clasificarlos automáticamente según su edad.

Aplicando conceptos clave de Programación Orientada a Objetos como:

Herencia (de la clase Persona a Paciente)

La encapsulación se aplica al atributo __motivo_de_consulta en la clase Paciente. Este atributo está declarado como privado usando doble guion bajo (__), lo que impide que se acceda directamente desde fuera de la clase. En su lugar, se gestionan los datos a través de métodos públicos como insertar_motivo_de_la_consulta() y mostrar_motivo_de_la_consulta(), protegiendo así la integridad del historial clínico.

El polimorfismo se muestra en el método mostrar_datos_de_la_persona(), el cual está definido inicialmente en la clase Persona y luego sobrescrito en la clase Paciente. Aunque el nombre del método es el mismo, el comportamiento cambia: en Persona muestra una presentación general, mientras que en Paciente adapta el mensaje al contexto clínico, lo que demuestra cómo un mismo método puede comportarse de manera distinta según el tipo de objeto que lo invoque.

![image](https://github.com/user-attachments/assets/517be174-eb85-424e-acae-3069838adf4a)
