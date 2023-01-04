function solution(n) {
    n = n.toString(3)
    n = n.split('').reverse().join('')
    n = Number.parseInt(n, '3')
    return n
}