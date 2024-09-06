function solution(arr) {
    var stk = [];
    let idx = 0;
    
    while (idx < arr.length) {
        if (stk.length === 0) {
            stk.push(arr[idx])
            idx++
        } else {
            if (stk[stk.length-1] < arr[idx]) {
                stk.push(arr[idx])
                idx++
            } else {
                stk.pop()
            }
        }
    }
    return stk;
}