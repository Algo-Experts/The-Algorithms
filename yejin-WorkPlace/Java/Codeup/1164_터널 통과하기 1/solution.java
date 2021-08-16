import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        int tunnel1 = scan.nextInt();
        int tunnel2 = scan.nextInt();
        int tunnel3 = scan.nextInt();
        
        if (tunnel1 <= 170 || tunnel2 <= 170 || tunnel3 <= 170) {
            System.out.println("CRASH");
        } else {
            System.out.println("PASS");
        }
        
    }

}