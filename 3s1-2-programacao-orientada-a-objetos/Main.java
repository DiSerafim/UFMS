
// Definição da classe Carro
class Carro {
    // Atributos
    String cor;
    String modelo;
    int ano;

    // Método para exibir informações do carro
    void exibirInfo() {
        System.out.println("Cor: " + cor + ", Modelo: " + modelo + ", Ano: " + ano);
    }
}

// Criando e utilizando um objeto da classe Carro
public class Main {
    public static void main(String[] args) {
        // Instanciando um objeto da classe Carro
        Carro meuCarro = new Carro();

        // Definindo os atributos do objeto
        meuCarro.cor = "Vermelho";
        meuCarro.modelo = "Gol";
        meuCarro.ano = 2020;

        // Exibindo informações do carro
        meuCarro.exibirInfo();
    }
}
