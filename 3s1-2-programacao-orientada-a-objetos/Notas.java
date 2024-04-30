import java.util.Scanner;
import java.util.HashSet;

public class Notas {
    public static void main(String[] args) {
        // input de entrada
        Scanner scanner = new Scanner(System.in);
        // Array que armazena as notas
        int[] notas = new int[10];
        
        // Ler as notas e soma
        int soma = 0;
        for (int i = 0; i < 10; i++) {
            notas[i] = scanner.nextInt();
            soma += notas[i];
        }

        // Valor médio
        int media = soma / 10;

        // Resultado da média
        System.out.println("Média: " + media);

        // Recebe notas acima da média
        HashSet<Integer> notasAcimaMedia = new HashSet<>();

        // Guarda notas acima da média
        for (int i = 0; i < 10; i++) {
            if (notas[i] > media) {
                notasAcimaMedia.add(notas[i]);
            }
        }

        // Mostra as notas acima da média
        System.out.print("Notas acima da média: ");
        for (int nota : notasAcimaMedia) {
            System.out.print(nota + " ");
        }
        System.out.println(); // Imprime uma nova linha
        
        // Fechar o scanner
        scanner.close();
    }
}
