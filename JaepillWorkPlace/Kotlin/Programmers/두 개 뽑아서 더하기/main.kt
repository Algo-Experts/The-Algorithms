class main {
    fun solution(numbers: IntArray): IntArray {
        val result: MutableList<Int> = arrayListOf()
        var sum = 0
        var i = 0
        var j = 0

        while (i < numbers.size - 1) {
            j = i + 1
            while (j < numbers.size) {
                sum = numbers[i] + numbers[j]
                result.add(sum)
                j++
            }
            i++
        }
        result.sort()
        return answers.distinct().toIntArray()
    }
}
