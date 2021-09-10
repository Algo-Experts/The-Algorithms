import Foundation

func solution(_ citations:[Int]) -> Int {
    var sortedNum = citations.sorted(by:>)
    for i in (1...sortedNum.count).reversed() {
        if sortedNum[i-1] >= i {
            return i
        }
    }
    return 0
}
