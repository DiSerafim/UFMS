public class SomaVetor {
    public static void main(String[] args) {
        int [] A = {1, 2, 3, 4, 5};
        int soma = 0;

        for (int i = 0; i < A.length; i++) {
            soma +=  A[i];
        }

        System.out.println("Soma: " + soma);
    }
}