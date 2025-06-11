/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package semana.pkg2;
/**
 *
 * @author HP - i5
 */
    // TODO code application logic here
        //Encapsulación
/**
 * Clase que representa a un estudiante y sus promedios académicos.
 * Aplica Encapsulamiento al proteger sus atributos.
 */
// Definición de la clase abstracta
 abstract class estudiante {  
    // Atributos protegidos o privados
    protected String nombre;  // Nombre del estudiante


    // Constructor
    public estudiante(String nombre) {  
        this.nombre = nombre;    
    }  

    // Métodos concretos (pueden tener implementación)
    public void metodoConcreto() {  
        System.out.println("Este es un método con implementación.");  
    }  

    // Métodos abstractos (deben ser implementados por las subclases)
    public abstract void metodoAbstracto();
}


 class Estudiante {  // Atributos protegidos: solo accesibles desde la misma clase o subclases
    protected String nombre;  // Nombre del estudiante
    protected float promedioMatematica;  // Promedio en Matemáticas
    protected float promedioCiencias;    // Promedio en Ciencias
    protected float promedioEstudios;    // Promedio en Estudios Sociales
    protected float promedioLenguaje;    // Promedio en Lenguaje

    // Constructor: inicializa los valores del estudiante al crear el objeto
    public Estudiante(String nombre,int curso, float promedioMatematica, float promedioCiencias, float promedioEstudios, float promedioLenguaje) {
        this.nombre = nombre;  // Asigna el nombre recibido al atributo interno
        this.promedioMatematica = promedioMatematica;  // Asigna el promedio de Matemáticas
        this.promedioCiencias = promedioCiencias;      // Asigna el promedio de Ciencias
        this.promedioEstudios = promedioEstudios;      // Asigna el promedio de Estudios Sociales
        this.promedioLenguaje = promedioLenguaje;      // Asigna el promedio de Lenguaje
    }

    // Método para mostrar los promedios individuales del estudiante
    public void atributos() {
        System.out.println("----Promedios de las materias----");  // Imprime encabezado
        System.out.println(nombre + ":");  // Muestra el nombre del estudiante
        System.out.println("- Matemáticas: " + promedioMatematica);  // Muestra promedio de Matemáticas
        System.out.println("- Ciencias: " + promedioCiencias);       // Muestra promedio de Ciencias
        System.out.println("- Estudios: " + promedioEstudios);       // Muestra promedio de Estudios Sociales
        System.out.println("- Lenguaje: " + promedioLenguaje);       // Muestra promedio de Lenguaje
    }

    //Este método aplica abstracción porque oculta el cálculo interno del promedio.
    // Método privado que calcula el promedio general entre las 4 materias
    public float calcularPromedio() {
        return (promedioMatematica + promedioCiencias + promedioEstudios + promedioLenguaje) / 4;
    }
    
    // Aplicación de la técnica de abstracción: este método simplifica el acceso al promedio general,
    // ocultando el detalle del cálculo al usuario de la clase.
    
    // Método que determina si el estudiante aprueba según la nota mínima exigida
    public void pasarmateria(int notaMinimaAprobacion) {
        float promedioTotal = calcularPromedio();  // Calcula el promedio general
        if (promedioTotal >= notaMinimaAprobacion) {  // Verifica si aprueba
            System.out.println("¡Felicidades! Pasaste con un promedio de: " + promedioTotal);
        } else {  // Si no alcanza la nota mínima
            System.out.println("Lo siento, tu promedio es " + promedioTotal + ", necesitas al menos " + notaMinimaAprobacion + " para aprobar.");
            System.out.println("Debes repetir el nivel");
        }
    }
}

//La abstracción consiste en mostrar solo los detalles importantes al exterior y ocultar la lógica interna.

//- Encapsulamiento: se aplica al mantener los atributos protected, lo que impide que otras clases accedan 
//directamente a los datos y los obliga a interactuar mediante los métodos definidos como atributos(), 
//calcularPromedio() y pasarmateria().


