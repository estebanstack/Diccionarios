import java.util.HashMap;
import java.util.Map;

public class Ejercicio5 {
    public static void main(String[] args) {
        // Crear el diccionario con las asignaturas y sus créditos
        Map<String, Integer> asignaturas = new HashMap<>();
        asignaturas.put("Matemáticas", 6);
        asignaturas.put("Física", 4);
        asignaturas.put("Química", 5);
        asignaturas.put("Sociales", 3);
        asignaturas.put("Biologia", 5);
        
        // Mostrar los créditos de cada asignatura
        int totalCreditos = 0;
        for (Map.Entry<String, Integer> entry : asignaturas.entrySet()) {
            System.out.println(entry.getKey() + " tiene " + entry.getValue() + " créditos.");
            totalCreditos += entry.getValue();
        }
        
        // Mostrar el total de créditos del curso
        System.out.println("El número total de créditos del curso es: " + totalCreditos);
    }
}
