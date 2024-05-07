import java.io.*;

public class TesteLeitura {
    public static void main(String[] args) {
        Cliente cliente;
        FileInputStream fluxo;
        ObjectInputStream objarq = null;

        try {
            fluxo = new FileInputStream("cliente.ser");
            objarq = new ObjectInputStream(fluxo);

            while(true) {
                cliente = (Cliente) objarq.readObject();
                System.out.println(cliente);
            }
        } catch (EOFException eofExc) {
            System.out.println("Chegou no fim do arquivo");
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
        finally{}
    }
}