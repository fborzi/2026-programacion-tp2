import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int numero = sc.nextInt();

        if (numero > 10) {
            System.out.println("El numero es mayor que 10");
        } else {
            System.out.println("El numero no es mayor que 10");
        }

        sc.close();
    }
}
