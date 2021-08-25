import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num = scan.nextInt();
        String print = "";
        
        if (num >= 90) {
            print = "A";
        } else if (num >= 80) {
            print = "B";
        } else if (num >= 70) {
            print = "C";
        } else if (num >= 60) {
            print = "D";
        } else {
            print = "F";
        }
        
        System.out.println(print);
    }

}