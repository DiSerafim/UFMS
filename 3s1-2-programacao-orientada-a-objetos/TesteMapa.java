import java.io.*;
import java.util.Map;
import java.util.TreeMap;

public class TesteMapa {
    public static void main(String[] args) {
        Map<Integer, String> mapa = new TreeMap<Integer, String>(); // Mapa
        mapa.put(455, "vermelho"); // elementos do mapa
        mapa.put(333, "branco"); // elementos do mapa
        mapa.put(678, "amarelo"); // elementos do mapa
        mapa.put(455, "azul"); // elementos do mapa

        try {
            FileOutputStream fluxo0ut = new FileOutputStream("myFile.ser"); // Cria o fluxo FileOutputStream
            ObjectOutputStream fOut = new ObjectOutputStream(fluxo0ut); // cria o fluxo ObjectOutputStream
            fOut.writeObject(mapa); // usa o método writeObject

            FileInputStream fluxoIn = new FileInputStream("myFile.ser"); // Cria o fluxo FileInputStream para fazer a leitura
            ObjectInputStream fIn = new ObjectInputStream(fluxoIn); // Cria o fluxo ObjectInputStream para fazer a leitura
            @SuppressWarnings("unchecked")
            TreeMap<Integer, String > mapaNovo = (TreeMap<Integer, String>)fIn.readObject(); // faz aleitura com readObject
            
            fIn.close(); // fecha
            fOut.close(); // fecha

            System.out.println(mapaNovo); // exibe o mapa
            
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
}