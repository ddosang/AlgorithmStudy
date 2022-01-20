import Foundation

func solution(_ absolutes:[Int], _ signs:[Bool]) -> Int {
    
    return absolutes
        .enumerated()
        .map { (index, value) in
            return signs[index] ? value : -value
        }
        .reduce(0, +)
    
}
