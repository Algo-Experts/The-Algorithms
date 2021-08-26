import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num1 = scan.nextInt();
        
        // 일반 if - else
        if (num1 % 2 == 0) {
            System.out.println("enjoy");
        } else {
            System.out.println("oh my god");
        }
        
        // 삼항연산자
        System.out.println(num1 % 2 == 0 ? "enjoy" : "oh my god");
    }

}