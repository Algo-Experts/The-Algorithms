import Foundation

func solution(_ nums:[Int]) -> Int {
    func isPrime(_ num: Int) -> Bool {
        if num < 3 {
            return num == 2 ? true : false
        } else {
            for i in 2..<num {
                if num % i == 0 {
                    return false
                }
            }
        }
        return true
    }
    
    var answer: Int = 0
    for i in 0..<nums.count-2 {
        for j in i+1..<nums.count-1 {
            for k in j+1..<nums.count {
                if isPrime(nums[i] + nums[j] + nums[k]) {
                    answer += 1
                }
            }
        }
    }
    
    return answer
}
