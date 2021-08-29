import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int year = scan.nextInt(); // 입력받은 년도
        int month = scan.nextInt(); // 입력받은 월
        int day = scan.nextInt(); // 입력받은 일
        
        int result = year - month + day; // 결과 값
        
        // if - else
        if (result % 10 == 0) {
            // 끝자리의 수를 확인 할 수 있는 건 나머지값을 확인해야함
            System.out.println("대박");
        } else {
            System.out.println("그럭저럭");
        }
        
        
        // 삼항연산자
        System.out.println(result % 10 == 0 ? "대박" : "그럭저럭");
        
        
    }

}