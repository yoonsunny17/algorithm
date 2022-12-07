function solution(my_string) {
    return [...my_string].map(a => a === a.toLowerCase() ? a.toUpperCase() : a.toLowerCase()).join('')
}