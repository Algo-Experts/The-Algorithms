1. https://programmers.co.kr/learn/courses/30/lessons/12918

### 생각의 전환.... try / catch문.....!
```JAVA
class Solution {
  public boolean solution(String s) {
      if(s.length() == 4 || s.length() == 6){ // 길이체크
          try{
              int x = Integer.parseInt(s); // 숫자로만 이뤄진 String이라면 오류 없이 변환이 가능.
              return true;
          } catch(NumberFormatException e){ // 문자가 포함되어 int로 변환이 안됨으로 오류로 인식.
              return false;
          }
      }
      else return false;
  }
}
```
   
