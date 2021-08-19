import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num = scan.nextInt();
        String print = "";
        
        if (num > 0) {
            print = "양수";
        } else if (num < 0) {
            print = "음수";
        } else {
            print = "0";
        }
        
        System.out.println(print);
    }

}