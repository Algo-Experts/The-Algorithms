1. 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12912

### readline( )
- 입력 받은 모든 값을 String으로 변환한다.


### 코틀린의 옵셔널
 - 코틀린은 스위프트와 같이 null safe를 위해 ? 또는 !!를 지원한다.
- #### ?
 var inputedStr: String? = leadline()?.toUpperCase()
 해석 : 입력값이 null이 아니라면 대문자로 바꿔 inputedStr에 저장하고,
           입력값이 null이라면 inputedStr는 null 이다.
- #### ?:
var inputedStr: String? = leadline()?.toUpperCase() ?: "none"
해석 : 입력값이 null이라면 우항은 "none"을 반환
* ?: 는 return,throw도 넣을 수 있다
- #### !!
val title: String = str!!
해석 : 강제로 null이 아님을 선언합니다.
         그리고 NPE이 발생하더라도 해당 라인을 명확히 지목해 줍니다.
- #### let
not null인 경우하면 지정된 구문을 실행합니다. 함수 사용시, 자신의 receiver 객체를 람다식 내부로 넘깁니다.
fun checkMail(email: String){
    email?.let {
        sendEmail(it)
    }
}

- #### String? type의 isNullOrBlank(), isNullOrEmpty()
fun String?.isNullOrBlack(): Boolean = 
    this = null || this.isBlank
형식이다. java라면 NPE가 발생하는 상황에서 동작시킬 수 있다.

### 풀이
1. 표준 입력으로 'n m'이 주어지므로, leadLine()으로 입력을 받아야 한다.
2. 절대 null이 발생할 수 없으므로, !!로 강제 null 처리를 한다.
3. split(' ')으로 입력받은 값을 공백을 기준으로 분리해 줍니다.
4. map(String::toInt)를 통해 String 타입을 toInt로 형변환해 줍니다.
5. 이제 a, b에는 각각 n, m이 입력된 상태입니다,
6. 가로의 길이 n은 a이므로 lenStar에 a개만큼 *을 입력해 저장합니다.
7. 세로의 길이 m은 b이므로, lenStar를 m만큼 println으로 출력합니다.
