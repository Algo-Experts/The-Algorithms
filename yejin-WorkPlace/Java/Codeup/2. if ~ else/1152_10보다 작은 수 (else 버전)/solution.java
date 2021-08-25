import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num = scan.nextInt();
        
        if (num < 10) {
            System.out.println("small");
        } else {
            System.out.println("big");
        }

    }

}

// 3항 연산자
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num = scan.nextInt();
        
        System.out.println(num < 10 ? "small" : "big");

    }

}