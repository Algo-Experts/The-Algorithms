import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num = scan.nextInt(); // 입력받은 수
        String print = ""; // 출력될 문구 저장소
        
        int numFirst = num / 10; // 1의 자리수
        int numSecond = (num % 10) * 10; // 2의 자리수
        
        numSecond += numFirst; // 1의 자리수와 2의자리수 바꿈
        
        
        numSecond *= 2;
        
        if (numSecond >= 100) {
            numSecond -= 100;
        }
        
        if (numSecond <= 50) {
            print = "GOOD";
        } else {
            print = "OH MY GOD";
        }
        
        System.out.println(numSecond);
        System.out.println(print);
        
    }

}