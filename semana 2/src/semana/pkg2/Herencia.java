/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package semana.pkg2;

/**
 *
 * @author HP - i5
 */
// Clase padre (superclase)
// Clase padre 
class Persona {
    protected String nombre; // Atributo común a todas las personas

    // Constructor que inicializa el nombre
    public Persona(String nombre) {
        this.nombre = nombre;
    }

    // Método que muestra el nombre de la persona
    public void mostrarNombre() {
        System.out.println("Nombre: " + nombre);
    }
}

// Clase hija o subclase que hereda de Persona usando 'extends'
 class Estudiante extends Persona {
    private float promedioMatematica, promedioCiencias, promedioEstudios, promedioLenguaje;

    // Constructor de Estudiante que reutiliza el constructor de Persona
    public Estudiante(String nombre, float promedioMatematica, float promedioCiencias, float promedioEstudios, float promedioLenguaje) {
        super(nombre); // Llamamos al constructor de la clase padre 'Persona'
        this.promedioMatematica = promedioMatematica;
        this.promedioCiencias = promedioCiencias;
        this.promedioEstudios = promedioEstudios;
        this.promedioLenguaje = promedioLenguaje;
    }

    // Método para calcular el promedio general
    public float calcularPromedio() {
        return (promedioMatematica + promedioCiencias + promedioEstudios + promedioLenguaje) / 4;
    }

    // Método para mostrar los promedios del estudiante
    public void mostrarPromedios() {
        mostrarNombre(); // Aprovechamos el método de la clase padre 'Persona'
        System.out.println("Promedios en materias:");
        System.out.println("- Matemáticas: " + promedioMatematica);
        System.out.println("- Ciencias: " + promedioCiencias);
        System.out.println("- Estudios: " + promedioEstudios);
        System.out.println("- Lenguaje: " + promedioLenguaje);
        System.out.println("Promedio general: " + calcularPromedio());
    }
}

    
