import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
         int notPromotion = scan.nextInt();
        int promotion = scan.nextInt();
        int promotionPrice = scan.nextInt();
        
        
        if (promotion - notPromotion > promotionPrice ) {
            System.out.println("advertise");
        } else if (promotion - notPromotion < promotionPrice) {
            System.out.println("do not advertise");
        } else {
            System.out.println("does not matter");
        }
        
        
    } // main
    
    

}