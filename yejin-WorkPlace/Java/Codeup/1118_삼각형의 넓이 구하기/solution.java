import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        
        Scanner scan = new Scanner(System.in);
        int bottom = scan.nextInt();
        int height = scan.nextInt();
        
        Double result = bottom * height / 2.0;
        
        System.out.println(String.format("%.1f", result));

    }

}