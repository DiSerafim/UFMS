import java.io.File;

public class ManipulacaoArquivos {
    public static void main(String[] args) {
        // Cria um diretório
        File directory = new File("./testeCriacaoDeDiretorioJava");
        directory.mkdir();

        // Verifica se um arquivo existe
        File file = new File("./testeCriacaoDeDiretorioJava/arq.txt");

        if (file.exists()) {
            System.out.println("O arquivo existe!");
        }

        // Listar arquivos em um diretório
        File[] files = directory.listFiles();

        for (File f : files) {
            System.out.println(f.getName());
        }
    }
}