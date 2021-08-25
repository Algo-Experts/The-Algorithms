import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num1 = scan.nextInt();
        int tot = 0;
        
        // 배열 선언 하지 않고 바로 값 찾기
        for (int i = 0; i < num1; i++) {
            tot += scan.nextInt();
        }
        
        System.out.println(tot);
        
    } // main

}