import Foundation

func solution(_ numbers:[Int]) -> Int {
    var answer = 0
    
    var check:[Int] = [0,1,2,3,4,5,6,7,8,9]
    
    for i in numbers.indices {
        check[numbers[i]] = 0
    }
    
    for num in check {
        answer += num
    }
    
    return answer
}
