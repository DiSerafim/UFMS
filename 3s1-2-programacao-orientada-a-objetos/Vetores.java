public class Vetores {
    public static void main(String[] args) {
        // declarando um vetor com até 10 valores (tamanho do vetor)
        int[] numeros = new int[10];
        
        // declarando um vetor com 4 valores (tamanho do vetor)
        int[] idades = {18, 21, 33, 45};

        // Armazenar elementos dentro de um vetor
        numeros[0] = 10;
        numeros[1] = 20;
        numeros[5] = 60;

        // Pegar elementos dentro do vetor
        System.out.println(numeros[0]);
        System.out.println(numeros[1]);
        System.out.println(numeros[5]);

        int num = numeros[0];
        System.out.println(num);

        System.out.println(idades + "" + "");

        // Estrutura de repetição
        for (int i = 0; i < numeros.length; i++) {
            System.out.println("Posição " + i);
            System.out.println(" Valor " + numeros[i]);
            // System.out.println(numeros[i]);
        }

        // Tentando incluir além do que já está programado.
        System.out.println(numeros[1000]);
        System.out.println("Exception in thread main java.lang.ArrayIndexOutOfBoundsException: Index 1000 out of bounds for length 10 at Vetores.main(Vetores.java:32)");
    }
}