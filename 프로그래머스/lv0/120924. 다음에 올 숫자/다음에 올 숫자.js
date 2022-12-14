function solution(common) {
    const dis = common[1] - common[0] === common[2] - common[1]
    if (dis) {
        return common[common.length-1] + (common[1] - common[0])
    } else {
        return common[common.length-1] * (common[1] / common[0])
    }
}