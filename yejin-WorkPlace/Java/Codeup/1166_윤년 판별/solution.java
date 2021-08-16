import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int year = scan.nextInt();
        
        if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)){
            System.out.println("yes");
        } else {
            System.out.println("no");
        }
        
        // 삼항연산자로도 가능하지만, 삼항연산자로 풀면 가독성이 떨어지기에 if문 사용
    }

}