function solution(dots) {
    const w = Math.max(...dots.map(a => a[0])) - Math.min(...dots.map(a => a[0]))
    const h = Math.max(...dots.map(a => a[1])) - Math.min(...dots.map(a => a[1]))
    return w*h
}