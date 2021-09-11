import Foundation

func solution(_ n:Int) -> Int
{
    var answer:Int = n+1
    while true{
        let num1 = String(n, radix: 2).map{$0}.filter{$0 == "1"}.count
        let num2 = String(answer, radix: 2).map{$0}.filter{$0 == "1"}.count
        if num1 == num2{
            break
        }
        answer += 1
    }
    
    return answer
}
