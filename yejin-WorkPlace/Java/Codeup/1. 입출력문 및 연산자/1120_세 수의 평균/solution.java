import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        
        int nums[] = new int[3];
        Double tot = 0.0;

        Scanner scan = new Scanner(System.in);
        for(int i = 0; i < nums.length; i++) {
            nums[i] = scan.nextInt();
            tot += nums[i];
        }
        
        System.out.println(String.format("%.2f", tot / nums.length));
        
        

    }

}