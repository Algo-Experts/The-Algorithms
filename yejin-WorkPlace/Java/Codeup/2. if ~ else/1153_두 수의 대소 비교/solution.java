import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num1 = scan.nextInt();
        int num2 = scan.nextInt();
        String print = "";
        
        if (num1 > num2) {
            print = ">";
        } else if (num1 < num2) {
            print = "<";
        } else {
            print = "=";
        }
        
        System.out.println(print);
        
        
    }

}