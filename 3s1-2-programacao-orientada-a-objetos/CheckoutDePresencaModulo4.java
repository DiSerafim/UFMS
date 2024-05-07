// 1. ✅Preencha o conjunto com as dez primeiras letras (char) do alfabeto, todas maiúsculas e ‘null’ no final.
// 2. ✅Preencha o mapa (Map) com as dez primeiras letras (char) do alfabeto como chave e com o índice de 0 a 9 para cada letra. Exemplo: (0:chave, A:valor).
// 3. ✅Percorra o conjunto imprimindo o valor de cada item no console e trate a exceção NullPointerException que irá ocorrer.
// 4. ✅Escreva um método chamado writeFile, que recebe como parâmetro uma String do nome do arquivo. No método use a classe FileWriter e BufferedWriter para escrever o texto “Erro ao percorrer coleção!” no arquivo com o nome recebido por parâmetro.
// 5. ✅Ao capturar a exceção, chame o método writeFile com o parâmetro “erro.txt”.
// 6. ✅Faça o uso de Classes Genéricas na definição e instanciação das coleções.
// 7. ✅Use o modificador de acesso “public” para todos os métodos.

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class CheckoutDePresencaModulo4 {
    public static void main(String[] args) {
        Set<Character> conjunto = new HashSet<>();
        Map<Character, Integer> mapa = new HashMap<>();

        preencherConjunto(conjunto);
        preencherMapa(mapa);

        // Percorre o conjunto e trata a exceção NullPointerException
        for (Character item : conjunto) {
            try {
                System.out.println(item);
            } catch (NullPointerException e) {
                // Chama o método writeFile com o parâmetro "erro.txt"
                writeFile("erro.txt");
            }
        }
    }

    // Preenche o conjunto com as 10 primeiras letras do alfabeto
    public static void preencherConjunto(Set<Character> conjunto) {
        for (char c = 'A'; c <= 'J'; c++) {
            conjunto.add(c);
        }
        conjunto.add(null); // adiciona ‘null’ no final.
    }

    // Preencher o mapa com as dez primeiras letras do alfabeto com a chave e o índice com o valor
    public static void preencherMapa(Map<Character, Integer> mapa) {
        for (int i = 0; i < 10; i++) {
            mapa.put((char) ('A' + i), i);
        }
    }    

    // Escreve no arquivo em caso de exceção
    public static void writeFile(String fileName) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(fileName))) {
            writer.write("Erro ao percorrer coleção!");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
