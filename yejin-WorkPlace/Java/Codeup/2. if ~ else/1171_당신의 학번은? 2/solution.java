import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int grade = scan.nextInt();
        int classNum = scan.nextInt();
        int number = scan.nextInt();
        
        String strGrade = Integer.toString(grade);
        String strClassNum = "";
        String strNumber = "";
        
        if (classNum < 10) {
            strClassNum = "0" + Integer.toString(classNum);
        } else {
            strClassNum = Integer.toString(classNum);
        }

        if (number < 10) {
            strNumber = "00" + Integer.toString(number);
        } else if (number < 100){
            strNumber = "0" + Integer.toString(number);
        } else {
            strNumber = Integer.toString(number);
        }
        
        System.out.println(strGrade + strClassNum + strNumber);
        
    }

}