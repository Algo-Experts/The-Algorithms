class main {
    fun solution(a: Int, b: Int): Long {
        var result = 0L

        if(a > b) {
            for(i in b.. a) {
                result += i
            }
        } else {
            for(i in a.. b) {
                result += i
            }
        }
        return result
    }
}