// const solution = (s1, s2) => s1.filter(v => s2.includes(v)).length

// 집합 활용
const solution = (s1, s2) => {
    return s1.length + s2.length - new Set([...s1, ...s2]).size
}

// const solution = (s1, s2) => s1.filter((a, i) => s2.includes(a)).length