function solution(id_list, report, k) {
    const newRepo = [...new Set(report)]
    const out = []
    const count = Array(id_list.length).fill(0) // 신고 수
    const mail = Array(id_list.length).fill(0) // 메일 수
    
    for (let re of newRepo){
        let a = re.split(" ")[0] // 유저 id
        let b = re.split(" ")[1] // 유저가 신고한 id
        let idxB = id_list.indexOf(b)
        count[idxB] += 1
        
        // 신고수가 k개 이상인 경우
        if (count[idxB] >= k){
            out.push(id_list[idxB])
        }
    }
    
    // 메일
    newRepo.map((re, idx) => {
        let a = re.split(" ")[0] // 유저 id
        let b = re.split(" ")[1] // 유저가 신고한 id
        
        // 신고한 id에 정지된 id가 있는지 확인
        if (out.indexOf(b) >= 0){
            // 신고한 id 중에 정지된 id가 있다면,
            // 해당 유저의 id_list에서의 인덱스를 구하고
            // mail의 해당 인덱스에 1 더하기
            let idx = id_list.indexOf(a)
            mail[idx] += 1
        }
    })
    
    return mail
}