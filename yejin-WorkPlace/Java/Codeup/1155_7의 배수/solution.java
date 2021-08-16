import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num1 = scan.nextInt();
        String print = "";
        
        
        // 일반 if - else
        if (num1 % 7 == 0) {
            print = "multiple";
        } else {
            print = "not multiple";
        }
        
        System.out.println(print);
        
        
        // 삼항연산자
        System.out.println(num1 % 7 == 0 ? "multiple" : "not multiple");
        
    }

}