import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		Double num1 = scan.nextDouble();
		Double num2 = scan.nextDouble();
		
		System.out.println(String.format("%.2f", (num1 * num2)));

	}

}