import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num1 = scan.nextInt();
        int count = 0;
        
        for (int i = 1; i <= num1; i += 10) {
            // 여기서 i += 10 을 한 이유는 1부터 시작할때 1 , 11, 21 ... 이런식으로 되기때문에 10씩 더해주면 1이 포함된 수를 확인 할 수 있다.
            count ++;
        }
        
        System.out.println(count);
        
    } // main

}