import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num1 = scan.nextInt();
        int[] nums = new int[num1];
        int tot = 0;
        
        for (int i = 0; i < num1; i++) {
            nums[i] = scan.nextInt();
            if (nums[i] % 5 == 0) {
                tot += nums[i];
            }
        }
        
        System.out.println(tot);
        
    } // main

}