import Foundation

func solution(_ n:Int) -> Int
{
    var answer:Int = 0
    let string = String(n).map{String($0)}
    for number in 0..<string.count{
       answer += Int(string[number])!
    }
    return answer
}
