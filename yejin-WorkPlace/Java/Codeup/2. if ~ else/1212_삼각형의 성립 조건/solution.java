import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
         int num1 = scan.nextInt();
        int num2 = scan.nextInt();
        int num3 = scan.nextInt();
        int max = 0;
        
        if(num1 >= num2){
            max = num2;
            num2 = num1;
            num1 = max;
        }
        if(num2 >= num3){
            max = num3;
            num3 = num2;
            num2 = max;
        }
        if(num1 >= num2){
            max = num2;
            num2 = num1;
            num1 = max;
        }
        if (num3 < num1 + num2) {
            System.out.println("yes");
        } else {
            System.out.println("no");
        }
        
        
    } // main

}
