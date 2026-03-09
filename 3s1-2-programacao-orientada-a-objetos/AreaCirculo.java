import java.util.Scanner;

public class AreaCirculo {
    public static void main(String[] args) {
        // Declaração de variáveis
        double raio, area;
        final double PI = 3.14159265;

        // Entrada de dados
        Scanner scanner = new Scanner(System.in);
        System.out.print("Informe o raio da circunferência: ");
        raio = scanner.nextDouble();
        
        // Cálculo da área
        area = PI * raio * raio;
        
        // Saída de dados
        System.out.println("A área da circunferência é: " + area);
        
        // Fechar o scanner
        scanner.close();
    }
}