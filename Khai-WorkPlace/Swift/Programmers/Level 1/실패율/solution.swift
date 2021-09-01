import Foundation

func solution(_ N:Int, _ stages:[Int]) -> [Int] {
    var rate = Array(repeating: 0, count: N + 1)

    for stage in stages {
        for i in 0..<stage {
            rate[i] += 1
        }
    }

    var result = [Int:Double]()
    for i in 0..<N {
        result.updateValue(Double(rate[i] - rate[i + 1]) / Double(rate[i]), forKey: i+1)
    }
    return result.sorted(by: <).sorted(by: {$0.value > $1.value}).map({ $0.key })
}
