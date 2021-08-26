import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num1 = scan.nextInt();
        int num2 = scan.nextInt();
        int tot = 0;
        
        for (int i = num1; i <= num2; i++) {
            if (i % 2 == 0) {
                tot -= i;
            } else {
                tot += i;
            }
        }
        
        System.out.println(tot);
        
        
    } // main

}