import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int hour = scan.nextInt();
        int minute = scan.nextInt();
        
        // 입력된 분이 30 보다 크거나 같으면 그대로 30분만 빼준다.
        if (minute >= 30) {
            minute -= 30;
        } else {
        // 입력된 분이 30 보다 작으면 시간을 1 빼준 후
            hour--;
            if (hour < 0) { // 시간이 0보다 작을 경우 23시로 출력
                hour = 23;
            } 
            minute += 30; // 30 을 더해준다.
            if (minute >= 60) { // 30을 더한 분이 60과 같거나 크면 0으로 출력한다.
                minute = 0;
            }
        }
        
        System.out.println(hour + " " + minute);
    }

}