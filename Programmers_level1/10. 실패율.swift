import Foundation

func solution(_ N:Int, _ stages:[Int]) -> [Int] {
    var challengers = Array(repeating: 0, count: N+2)
    var entered = 0
    let personCount = stages.count
    var failable = [Int:Double]()
    
    
    for stage in stages {
        challengers[stage] += 1
    }
    
    for i in stride(from: N+1, to: 0, by: -1) {
        entered += challengers[i]

        if i <= N {
            if entered == 0 {
                failable[i] = 0
            } else {
                failable[i] = Double(challengers[i]) / Double(entered)
            }
        }
    }
    
    return Array(failable.keys).sorted {
        if failable[$0]! > failable[$1]! {
            return true
        } else if failable[$0]! == failable[$1]! {
            return $0 < $1
        } else {
            return false
        }
    }
}
