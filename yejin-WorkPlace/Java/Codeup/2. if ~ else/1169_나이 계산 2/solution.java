import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int age = scan.nextInt(); // 입력받은 나이
        int gender = 0; // 성별 저장될 공간
        int year = 2012; // 기준 년도
        
        for (int i = 1; i < age; i++ ) { // 나이만큼 기준년도를 태어난 년도까지 빼준다.
            year--;
        }
        
        if (year < 2000) { // 태어난 년도가 구해지면 주민번호의 성별을 구하기 위해 검사를 해준다.
            gender = 1;
        } else {
            gender = 3;
        }
        
        year %= 100; // 년도의 2자리숫자만 구하기 위해 나머지를 구해준다.
        
        System.out.println(year + " " + gender);
        
    }

}