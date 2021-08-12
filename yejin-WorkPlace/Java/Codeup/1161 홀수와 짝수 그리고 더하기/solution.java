import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int num1 = scan.nextInt();
		int num2 = scan.nextInt();
		int result = 0;

		String oddNum1, oddNum2, strResult;

		result = num1 + num2;

		System.out.println((oddNum1 = num1 % 2 == 0 ? "짝수" : "홀수" ) + "+" + (oddNum2 = num2 % 2 == 0 ? "짝수" : "홀수") + "=" + (strResult = result % 2 == 0 ? "짝수" : "홀수"));
	}

}
