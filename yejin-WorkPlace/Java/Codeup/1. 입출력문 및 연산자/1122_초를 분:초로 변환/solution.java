import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        int num1 = scan.nextInt();
        
        int minute = num1 / 60;
        int second = num1 % 60;
        
        System.out.println(minute + " " + second);
        
    }

}