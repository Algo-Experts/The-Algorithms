import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Double num1 = scan.nextDouble(); // 실수와 정수 같이 입력받기위해 Double로 선언
        String print = ""; // 출력물 저장 변수
        
        
        // 일반 if - else
        if ((30 <= num1 && num1 <= 40) || (60 <= num1 && num1 <= 70)){
            // && 는 '그리고'라는 뜻임으로 두 조건에 다 true여야지 조건문이 성립된다.
            // || 는 '또는'라는 뜻임으로 두 조건 중 하나만 true여도 조건문 성립이 가능하다.
            print = "win";
        } else {
            print = "lose";
        }
        
        System.out.println(print);
        
        
        // 삼항연산자
        System.out.println(((30 <= num1 && num1 <= 40) || (60 <= num1 && num1 <= 70)) ? "win" : "lose");
        
    }

}