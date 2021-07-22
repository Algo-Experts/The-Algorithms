class main {
  fun solution(arr1: Array<IntArray>, arr2: Array<IntArray>): Array<IntArray> {
      return Array(arr1.size) {
          i ->
          IntArray(arr1[i].size) {
              j ->
              arr1[i][j] + arr2[i][j]
          }
      }
  }
}
