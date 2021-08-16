import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int year = scan.nextInt(); // 생년월일
        int gender = scan.nextInt(); // 성별
        int age = 0; // 나이 저장될 변수 초기화
        
        year /= 10000; // 생년월일의 연도만 가져오기 위해 나눠준다.
        
        if (gender == 1 || gender == 2) { // 이전에 입력받은 성별로 구분해준다.
            year += 1900;
        } else {
            year += 2000;
        }
        
        
        for (int i = year; i <= 2012; i++) { // 기준인 2012까지 될동안 나이를 더해준다.
            age++;
        }
        System.out.println(age);
        
        
    }

}