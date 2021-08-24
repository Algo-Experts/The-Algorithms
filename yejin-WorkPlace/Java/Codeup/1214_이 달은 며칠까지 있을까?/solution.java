import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
         int year = scan.nextInt();
        int month = scan.nextInt();
        int printMonth = 0;
        
        
        if (month == 2) {
            if (month % 2 == 0) {
                if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)){
                    printMonth = 29;
                } else {
                    printMonth = 28;
                }
            }
        } else if (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) {
            printMonth = 31;
        } else {
            printMonth = 30;
        }
        
        System.out.println(printMonth);
        
        
    } // main
    
    

}