import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num1 = scan.nextInt(); // 첫번째 숫자
        int num2 = scan.nextInt(); // 두번째 숫자
        int result = num1 + num2; // 첫번째 숫자와 두번째숫자의 합
        
        String numStr1 = "";
        String numStr2 = "";
        String resultStr = "";
        
        // 일반 if - else
        if (num1 % 2 == 0) {
            numStr1 = "짝수";
        } else {
            numStr1 = "홀수";
        }
        
        if (num2 % 2 == 0) {
            numStr2 = "짝수";
        } else {
            numStr2 = "홀수";
        }
        
        if (result % 2 == 0) {
            resultStr = "짝수";
        } else {
            resultStr = "홀수";
        }
        
        System.out.println(numStr1 + "+" + numStr2 + "=" + resultStr);
        
        
        // 삼항연산자
        numStr1 = num1 % 2 == 0 ? "짝수" : "홀수";
        numStr2 = num2 % 2 == 0 ? "짝수" : "홀수";
        resultStr = result % 2 == 0 ? "짝수" : "홀수";
        
        System.out.println(numStr1 + "+" + numStr2 + "=" + resultStr);
        
    }

}