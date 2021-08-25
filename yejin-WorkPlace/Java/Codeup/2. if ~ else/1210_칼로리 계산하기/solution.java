import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num1 = scan.nextInt();
        int num2 = scan.nextInt();
        
        int calorie = 0;
        
        
        switch (num1) {
        case 1:
            calorie += 400;
            break;
        case 2:
            calorie += 340;
            break;
        case 3:
            calorie += 170;
            break;
        case 4:
            calorie += 100;
            break;
        default:
            calorie += 70;
            break;
        }
        System.out.println(calorie);
        
        switch (num2) {
        case 1:
            calorie += 400;
            break;
        case 2:
            calorie += 340;
            break;
        case 3:
            calorie += 170;
            break;
        case 4:
            calorie += 100;
            break;
        default:
            calorie += 70;
            break;
        }
        System.out.println(calorie);
        
        if (calorie > 500) {
            System.out.println("angry");
        } else {
            System.out.println("no angry");
        }
        
    } // main

}