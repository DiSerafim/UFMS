package OrienJava;
   
public class Caneta {
    // atributos
    boolean tampada;
    String marca;
    String cor;
    
    // métodos
    public void tampar() {
        tampada = true;
    }

    public void destampar() {
        tampada = false;
    }

    public void escrever() {
        if (tampada == true) {
            System.out.println("Erro, não foi possível escrever com a caneta tampada!");
        } else {
            System.out.println("Agora você pode escrever com a caneta!");
        }
    }
}