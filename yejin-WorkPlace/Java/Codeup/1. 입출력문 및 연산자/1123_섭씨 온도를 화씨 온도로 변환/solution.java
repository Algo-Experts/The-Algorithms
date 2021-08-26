import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        int num1 = scan.nextInt();
        
        Double result = ((double) 9 / 5 * num1 + 32);
        
        System.out.println(String.format("%.3f", result));
        
    }

}