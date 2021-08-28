import Foundation

func solution(_ w:Int, _ h:Int) -> Int64{
    var num1 = w
    var num2 = h
    while num1%num2 != 0 {
       let x = num1%num2
       num1 = num2
       num2 = x
    }
    return Int64(w*h-(w+h-num2))
}
