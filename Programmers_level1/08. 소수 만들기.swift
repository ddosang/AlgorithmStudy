import Foundation
func isPrime(num: Int) -> Bool {
    if num < 2 {
        return false
    }
    
    let root = Int(pow(Double(num), 0.5))
    for i in 2..<root+1 {
        if num % i == 0 {
            return false
        }
    }
    return true
}

func solution(_ nums:[Int]) -> Int {
    var answer = 0

    for i in nums.indices {
        for j in i+1..<nums.count {
            for k in j+1..<nums.count {
                if isPrime(num: nums[i] + nums[j] + nums[k]) {
                    answer += 1
                }
            }
        }
    }
    
    return answer
}
