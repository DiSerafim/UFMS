public class Exceptions {
    public static void main(String[] args) {
        String a = "a";
        String b = "b";

        int x = soma(a, b);

        System.out.println(x);
    }

    public static int soma(String a, String b) {
        try {
            int x = Integer.parseInt(a) + Integer.parseInt(b);

            System.out.println("Soma realizada.");

            return x;
        } catch (NumberFormatException e) {
            return 0;
        } finally {

        }
    }
}
