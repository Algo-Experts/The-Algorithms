import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int grade = scan.nextInt();
        int classNum = scan.nextInt();
        int number = scan.nextInt();
        
        // 출력하기 위해 String으로 형변환을 해준다.
        String strGrade = Integer.toString(grade);
        String strClassNum = Integer.toString(classNum);
        String strNumber = "";
        
        
        if (number < 10) { // 입력받은 number가 10보다 작으면
            strNumber = "0" + Integer.toString(number);
        } else {
            strNumber = Integer.toString(number);
        }
        
        System.out.println(strGrade + strClassNum + strNumber);
        
    }

}