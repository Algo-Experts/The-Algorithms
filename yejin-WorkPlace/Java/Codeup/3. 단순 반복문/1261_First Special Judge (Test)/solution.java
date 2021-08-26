import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int[] nums = new int[10]; // 10개 수 저장 배열
        Boolean isCheck = false; // 5의 배수 여부확인
        
        for (int i = 0; i < nums.length; i++) {
            nums[i] = scan.nextInt();
        }
        
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] % 5 == 0) {
                isCheck = true; // 5의 배수가 있는 경우 true 값
                System.out.println(nums[i]);
                break;
            } 
        }
        
        if (isCheck == false) {
            System.out.println("0");
        }
        
    } // main

}