import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int time = scan.nextInt();
        int score = scan.nextInt();
        
        for (int i = time; i < 90; i += 5) {
            score++;
        }
        
        System.out.println(score);
    }

}
