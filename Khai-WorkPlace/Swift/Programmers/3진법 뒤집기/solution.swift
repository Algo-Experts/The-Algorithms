import Foundation

func solution(_ n:Int) -> Int {
    let result = String(n,radix: 3)
    return Int(String(result.reversed()),radix:3)!
}
