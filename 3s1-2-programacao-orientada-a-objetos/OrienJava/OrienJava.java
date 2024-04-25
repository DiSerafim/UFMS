package OrienJava;

public class OrienJava{
   
    public static void main(String[] args) {
        Caneta c1 = new Caneta();
        c1.cor = "Azul";
        c1.marca = "Bic";
        c1.tampada = false;
        c1.tampar();
        c1.escrever();
    }
}