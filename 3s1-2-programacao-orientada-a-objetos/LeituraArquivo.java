import java.io.FileReader;
import java.io.IOException;

public class LeituraArquivo {
    public static void main(String[] args) {
    try {
    FileReader reader = new FileReader("modulo4-unid4.txt");
    int character;
    while ((character = reader.read()) != -1) {
    System.out.print((char) character);
    }
    reader.close();
    } catch (IOException e) {
    e.printStackTrace();
    }
    }
   }