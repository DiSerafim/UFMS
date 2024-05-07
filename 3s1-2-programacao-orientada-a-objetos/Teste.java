import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;

public class Teste {
    public static void main(String[] args) {
        Cliente cliente = new Cliente("293894930", "Daniel");
        FileOutputStream fluxo;

        try {
            fluxo = new FileOutputStream("cliente.ser");
            ObjectOutputStream objarq = new ObjectOutputStream(fluxo);
            objarq.writeObject(cliente);

            objarq.close();
            System.out.print("Arquivo gravado.");
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }    
}
