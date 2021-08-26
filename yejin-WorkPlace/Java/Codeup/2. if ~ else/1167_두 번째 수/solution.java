import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int nums[] = new int[3]; // 배열 선언 및 초기화
        
        for (int i = 0; i < nums.length; i++) {
            nums[i] = scan.nextInt(); // 배열 저장
        }
        
        Arrays.sort(nums); // 배열 오름차순 정렬
        
        System.out.println(nums[1]); // 두번째 숫자 출력 (배열의 인덱스는 0부터 시작)
        
        
    }

}