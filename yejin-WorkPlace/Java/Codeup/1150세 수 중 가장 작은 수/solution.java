import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int[] nums = new int[3];
		int min = Integer.MAX_VALUE;

		for (int i = 0; i < nums.length; i++) {
			nums[i] = scan.nextInt();
			if (min > nums[i]) {
				min = nums[i];
			}
		}

		System.out.println(min);
	}

}
