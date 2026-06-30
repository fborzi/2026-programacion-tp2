import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int x = sc.nextInt();
        int y = sc.nextInt();

        if (x > y) {
            System.out.println(x + " es mayor que " + y);
        } else if (x < y) {
            System.out.println(x + " es menor que " + y);
        } else {
            System.out.println(x + " es igual a " + y);
        }

        sc.close();
    }
}
