function solution(k, score) {
    var answer = []
    var jundang = []
    
    for (let sc of score) {
        jundang.push(sc)
        jundang.sort((a, b) => b-a)        
        
        jundang.length < k ? answer.push(jundang[jundang.length - 1]) : answer.push(jundang[k - 1])
    }
    
    return answer
    
    
}