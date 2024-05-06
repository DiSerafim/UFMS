import java.io.FileWriter;
import java.io.IOException;

public class EscritaArquivo {
    public static void main(String[] args) {
        try {
            FileWriter writer = new FileWriter("escrita-arquivo.txt");
            writer.write("Escrita em Arquivos em Java.");
            System.out.println(" ");
            
            writer.write("EscritaArquivo.java");
            System.out.println(" ");
            writer.write("Olá, mundo!");
            // escrever mais texto

            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}