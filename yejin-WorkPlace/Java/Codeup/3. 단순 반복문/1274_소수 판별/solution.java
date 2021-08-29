import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num1 = scan.nextInt();
        int check = 0;
        
        for (int i = 1; i <= num1; i++) {
            if (num1 % i == 0) {
                check ++ ;
            }
        }
        
        if (check == 2) {
            System.out.println("prime");
        } else {
            System.out.println("not prime");
        }
        
        
    } // main

}