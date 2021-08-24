import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
         Double num1 = scan.nextDouble();
         Double num2 = scan.nextDouble();
         Double num3 = scan.nextDouble();
         Double num4 = scan.nextDouble();
        
        
        if ((num1 / num2) > (num3 / num4)) {
            System.out.println(">");
        } else if ((num1 / num2) == (num3 / num4)) {
            System.out.println("=");
        } else {
            System.out.println("<");
        }
        
        
    } // main

}