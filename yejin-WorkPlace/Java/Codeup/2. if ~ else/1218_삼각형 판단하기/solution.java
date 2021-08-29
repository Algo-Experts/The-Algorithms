import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
         int num1 = scan.nextInt();
        int num2 = scan.nextInt();
        int num3 = scan.nextInt();
        
        
        if (num3 >= num1 + num2) {
            System.out.println("삼각형아님");
        } else if (num1 == num2 && num2 == num3 && num1 == num3) {
            System.out.println("정삼각형");
        } else if (num1 == num2  ||  num2 == num3 || num1 == num3) {
            System.out.println("이등변삼각형");
        } else if ((num1 * num1) + (num2 * num2) == (num3 * num3)) {
            System.out.println("직각삼각형");
        } else  {
            System.out.println("삼각형");
            
        }
        
        
        
    } // main
    
    

}