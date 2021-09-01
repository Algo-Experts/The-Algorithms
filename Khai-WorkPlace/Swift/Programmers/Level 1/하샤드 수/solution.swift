func solution(_ x:Int) -> Bool {
    var sum=0
    var temp=x
    
    while temp != 0{
        sum+=temp%10
        temp/=10
    }
    
    return x%sum==0
}
