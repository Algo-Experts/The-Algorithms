import Foundation

func solution(_ numbers:[Int]) -> [Int] {
    
    var a:Set<Int>=[]
    
    for i in 0..<numbers.count{
        for j in i+1..<numbers.count{
            a.insert(numbers[i]+numbers[j])
        }
    }
    
    return a.sorted()
}
