function solution(lottos, win_nums) {
    // 민우 로또에서 당첨번호랑 일치하는 번호 몇개?
    const match = lottos.filter(lotto => win_nums.includes(lotto)).length
    
    // 민우 로또에 0 개수 몇개?
    const zero = lottos.filter(lotto => lotto === 0).length
    
    // 7 - match = 얼마나 못 맞췄는가
    const lowest = 7 - match >= 6 ? 6 : 7 - match
    const highest = lowest - zero < 1 ? 1 : lowest - zero
    
    return [highest, lowest]
}