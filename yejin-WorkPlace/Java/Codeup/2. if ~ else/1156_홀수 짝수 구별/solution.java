import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num1 = scan.nextInt();
        String print = "";
        
        
        // 일반 if - else
        if (num1 % 2 == 0) {
            print = "even";
        } else {
            print = "odd";
        }
        
        System.out.println(print);
        
        
        // 삼항연산자
        System.out.println(num1 % 2 == 0 ? "even" : "odd");
        
    }

}