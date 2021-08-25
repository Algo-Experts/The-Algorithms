import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num1 = scan.nextInt();
        int num2 = scan.nextInt();
        int tot = 0;
        
        
        if (num1 % 2 == 0) {
            tot += (num1 / 2) * 10;
        } else {
            tot += (num1 + 1) / 2;
        }
        
        if (num2 % 2 == 0) {
            tot += (num2 / 2) * 10;
        } else {
            tot += (num2 + 1) / 2;
        }
        
        System.out.println(tot);
        
        
    } // main

}