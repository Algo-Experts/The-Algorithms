class main {
    fun solution(n: Int): Int {
        var input = n
        var result = 0

        while (input > 0) {
            answer += input % 10
            input /= 10
        }
        return result
}