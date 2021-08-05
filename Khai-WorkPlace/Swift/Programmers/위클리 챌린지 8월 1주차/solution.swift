import Foundation

func solution(_ price:Int, _ money:Int, _ count:Int) -> Int64{
    var answer:Int64 = -1
    var temp:Int64 = 0
    
    for i in 1...count{
        temp += Int64(price * i)
    }
    
    return money >= temp ? 0 : temp - Int64(money)
}
