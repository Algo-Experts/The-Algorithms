import Foundation

func solution(_ board:[[Int]], _ moves:[Int]) -> Int {
    var board = board
    var array: [Int] = []
    var count: Int = 0
    
    for i in moves {
        for j in 0..<board.count {
            let temp = board[j][i-1]
            if temp != 0 {
                board[j][i-1] = 0
                if array.last == target {
                    array.removeLast()
                    count += 1
                } else {
                    array.append(temp)
                }
                break
            }
        }
    }
    
    return count * 2
}
