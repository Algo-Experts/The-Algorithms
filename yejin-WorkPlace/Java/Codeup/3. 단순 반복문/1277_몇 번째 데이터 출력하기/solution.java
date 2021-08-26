import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num1 = scan.nextInt();
        int number = 0;
        int first = 0;
        int mid = 0;
        int last = 0;
        
        for (int i = 1; i <= num1; i++) {
            number = scan.nextInt();
            if (i == 1) { // 첫번째 숫자
                first = number;
            }
            if (i == (num1 + 1) / 2) { // 가운데 숫자 ( num1 홀수일 수 도있으니 +1 해준다. )
                mid = number;
            }
            
            if (i == num1) { // 마지막 숫자
                last = number;
            }
        }
        
        
        System.out.println(first + " " + mid + " " + last);
        
        
    } // main

}