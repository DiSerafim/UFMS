import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class ManipulacaoArquivosBinarios {
    public static void main(String[] args) {
        try {
            FileInputStream input = new FileInputStream("./img/classe.jpeg");
            FileOutputStream output = new FileOutputStream("./img/copia_classe.jpeg");

            byte[] buffer = new byte[1024];
            int bytesRead;
            while ((bytesRead = input.read(buffer)) != -1) {
                output.write(buffer, 0, bytesRead);
            }

            input.close();
            output.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}