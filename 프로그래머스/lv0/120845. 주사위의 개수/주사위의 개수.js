function solution(box, n) {
    const arr = [...box].map((a) => Math.floor(a / n), '')
    return arr[0] * arr[1] * arr[2]
}