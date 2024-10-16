// js에서 set 크기는 size!
function solution(nums) {
    let mine = Math.round(nums.length / 2)
    let kinds = new Set(nums)
    
    return Math.min(mine, kinds.size)
}