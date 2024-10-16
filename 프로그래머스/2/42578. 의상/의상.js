function solution(clothes) {
    let ans = 1
    
    let dict = {}
    
    for (c of clothes) {
        if (!Object.keys(dict).includes(c[1])) {
            dict[c[1]] = 1
        } else {
            dict[c[1]]++
        }
    }
    
    for (v of Object.values(dict)) {
        ans += ans * v
    }
    

    return ans-1;
}