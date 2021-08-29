import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num = scan.nextInt();
        int numResult = 0;
        
        if (num <= 13) {
            switch (num) {
            case 1:
                System.out.println(num + "st");
                break;
            case 2:
                System.out.println(num + "nd");
                break;
            case 3:
                System.out.println(num + "rd");
                break;
            default:
                System.out.println(num + "th");
                break;
            }
        } else {
            numResult = num % 10;
            switch (numResult) {
            case 1:
                System.out.println(num + "st");
                break;
            case 2:
                System.out.println(num + "nd");
                break;
            case 3:
                System.out.println(num + "rd");
                break;
            default:
                System.out.println(num + "th");
                break;
            }
        }
        
    }

}