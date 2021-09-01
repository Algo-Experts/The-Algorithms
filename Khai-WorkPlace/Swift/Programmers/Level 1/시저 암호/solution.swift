func solution(_ s:String, _ n:Int) -> String {
    let alphabet = Array("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    return String( s.map {
        guard let index = alphabet.firstIndex(of: Character($0.uppercased()) ) else {
            return $0
        }
        let result = alphabet[(index + n) % alphabet.count]
        return  $0.isUppercase ? result : Character(result.lowercased())
    })
}
