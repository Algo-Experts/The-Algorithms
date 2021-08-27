import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num1 = scan.nextInt();
        int num2 = scan.nextInt();
        
        for (int i = 1; i <= num2; i++) {
            for (int j = 1; j <= num1; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}