import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num1 = scan.nextInt();
        int count = 0;
        
        while (num1 != 0) {
            num1 /= 10;
            count++;
        }
        
        System.out.println(count);
        
        
    } // main

}