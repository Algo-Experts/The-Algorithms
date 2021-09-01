import Foundation

func solution(_ left:Int, _ right:Int) -> Int {
    var nums:[Int]=[]
    var sum=0
    
    for i in left...right{
        for j in 1...i{
            if i%j==0{
                nums.append(j)
            }
        }
        if nums.count%2==0{
            sum+=i
        }else{
            sum-=i
        }
        nums.removeAll()
    }
    
    return sum
}
