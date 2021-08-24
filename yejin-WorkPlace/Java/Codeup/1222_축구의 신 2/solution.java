import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
         int time = scan.nextInt();
        int class1 = scan.nextInt();
        int class2 = scan.nextInt();
        
        
        for (int i = time; i < 90; i+=5) {
            class1++;
        }
        
        if (class1 > class2) {
            System.out.println("win");
        } else if (class1 == class2) {
            System.out.println("same");
        } else {
            System.out.println("lose");
        }
        
        
        
    } // main
    
    

}