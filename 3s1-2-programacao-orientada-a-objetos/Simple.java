import java.util.Scanner;

class Simple{  
    public static void main(String args[]){  
        Scanner s = new Scanner(System.in);
        int[] v = new int[10];
        int sum = 0;
        for (int i = 0; i < v.length; i++) {
v[i] = s.nextInt();
sum += v[i];
        }
        System.out.println("Média:" + (sum / v.length));
        s.close();
    }
}