import Foundation

func solution(_ numbers:[Int]) -> String {
    var sorted = numbers.map{String($0)}
    sorted.sort{ $0+$1 > $1+$0 }
    
    let answer = sorted.joined()
    if let num = Int(answer) { return String(num) }
    return answer
}
