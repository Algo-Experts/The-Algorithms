import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int nums[] = new int[3]; // 3수를 저장할 배열 선언
        
        for (int i = 0; i < nums.length; i++) { // for문을 돌며 3번 숫자를 입력 받는다.
            nums[i] = scan.nextInt();
        }
        
        Arrays.sort(nums); // 오름차순 정렬
        
        System.out.println(nums[0] + " " + nums[1] + " " + nums[2]);
    }

}