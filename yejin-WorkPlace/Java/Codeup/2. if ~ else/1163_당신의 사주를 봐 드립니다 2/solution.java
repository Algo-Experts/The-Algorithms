import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int year = scan.nextInt(); // 입력받은 년도
        int month = scan.nextInt(); // 입력받은 월
        int day = scan.nextInt(); // 입력받은 일
        
        int result = year + month + day; // 결과 값
        
        result %= 1000; // 결과 값의 100의 자리 숫자를 구하기 위해 나머지값을 구한다.
        
        result /= 100; // 100의 자리 숫자가 짝수인지 홀수인지 확인하기 위해 100의 자리수만 따로 구한다.

        // if - else
        // 짝수 또는 홀수인지 확인한다.
        if (result % 2 == 0) {
            System.out.println("대박");
        } else {
            System.out.println("그럭저럭");
        }
        
        
        // 삼항연산자
        // 짝수 또는 홀수인지 확인한다.
        System.out.println(result % 10 == 0 ? "대박" : "그럭저럭");
        
        
    }

}