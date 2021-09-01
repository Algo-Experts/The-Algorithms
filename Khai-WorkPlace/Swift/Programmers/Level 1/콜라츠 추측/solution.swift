func solution(_ num:Int) -> Int {
    var count = 0
    var number = num
    
    while number != 1{
        if(number%2==0){
            number = number/2
        }else{
            number = number*3+1
        }
        count += 1
    }
    
    return count >= 500 ? -1 : count
}
