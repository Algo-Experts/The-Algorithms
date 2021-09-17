import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        String listStr= "";

        for(int i=0; i<a; i++){
            listStr += "*";  
        }

        for(int i=0; i<b; i++){
            System.out.println(listStr);   
        }
    }
}

// 다른 사람의 풀이 1
// import java.util.Scanner;
// import java.util.stream.IntStream;

// public class Solution {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         int a = sc.nextInt();
//         int b = sc.nextInt();

//         StringBuilder sb = new StringBuilder();
//         IntStream.range(0, a).forEach(s -> sb.append("*"));
//         IntStream.range(0, b).forEach(s -> System.out.println(sb.toString()));
//     }
// }


// 다른 사람의 풀이 2
// import java.util.Scanner;

// public class Solution {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         int a = sc.nextInt();
//         int b = sc.nextInt();

//         StringBuilder sb = new StringBuilder();
//         for(int i=0; i<a; i++){
//             sb.append("*");
//         }
//         for(int i=0; i<b; i++){
//             System.out.println(sb.toString());
//         }
//     }
// }