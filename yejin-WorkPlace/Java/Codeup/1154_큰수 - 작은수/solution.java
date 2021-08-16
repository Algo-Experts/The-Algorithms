import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num1 = scan.nextInt();
        int num2 = scan.nextInt();
        
        
        // 일반 if - else 
        if (num1 > num2) {
            System.out.println(num1 - num2);
        } else {
            System.out.println(num2 - num1);
        }
        
        // 3항 연산자
        System.out.println(num1 > num2 ? num1 - num2 : num2 - num1);
        
    }

}