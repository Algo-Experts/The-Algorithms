import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num1 = scan.nextInt();
        int[] nums = new int[num1];
        int max = 0;
        
        for (int i = 0; i < nums.length; i++) {
            nums[i] = scan.nextInt();
            if (nums[i] > max) {
                max = nums[i];
            }
        }
        
        System.out.println(max);
        
    } // main

}