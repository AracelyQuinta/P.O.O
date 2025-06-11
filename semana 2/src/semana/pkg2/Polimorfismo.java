/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package semana.pkg2;

// CLASE ABSTRACTA: Define una estructura común para Estudiantes y Profesores
abstract class Persona {
    protected String nombre;

    public Persona(String nombre) {
        this.nombre = nombre;
    }

    // Método abstracto que las clases hijas deben sobrescribir
    public abstract void mostrarInformacion();

    public String getNombre() {
        return nombre;
    }
}

// CLASE HIJA: Estudiante
class Estudiante extends Persona {
    private float promedioMatematica, promedioCiencias, promedioEstudios, promedioLenguaje;

    public Estudiante(String nombre, float m, float c, float e, float l) {
        super(nombre); // Llamamos al constructor de la superclase
        this.promedioMatematica = m;
        this.promedioCiencias = c;
        this.promedioEstudios = e;
        this.promedioLenguaje = l;
    }

    @Override
    public void mostrarInformacion() {
        System.out.println("Soy un estudiante llamado/a " + getNombre() + " y mi promedio es " + calcularPromedio());
    }

    private float calcularPromedio() {
        return (promedioMatematica + promedioCiencias + promedioEstudios + promedioLenguaje) / 4;
    }
}

// CLASE HIJA: Profesor
class Profesor extends Persona {
    private String materia;

    public Profesor(String nombre, String materia) {
        super(nombre);
        this.materia = materia;
    }

    @Override
    public void mostrarInformacion() {
        System.out.println("Soy un profesor llamado/a " + getNombre() + " y enseño " + materia);
    }
}

// CLASE PRINCIPAL: Prueba el polimorfismo
public class Polimorfismo {
    public static void main(String[] args) {
        Persona estudiante = new Estudiante("Aracely", 90, 85, 88, 92);
        Persona profesor = new Profesor("María", "Matemáticas");
            
        estudiante.mostrarInformacion();  // Se ejecuta la versión específica de `Estudiante`
        profesor.mostrarInformacion();    // Se ejecuta la versión específica de `Profesor`
    }
}

