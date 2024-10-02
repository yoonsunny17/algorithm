// 분 단위로 바꿔주기
function transTime(arr) {
    let calc = Number(arr[0]) * 60 + Number(arr[1])
    return calc
}

function solution(video_len, pos, op_start, op_end, commands) {
    var answer = '';

    let [v, p, op_s, op_e] = [video_len.split(":"), pos.split(":"), op_start.split(":"), op_end.split(":")]
    
    v = transTime(v)
    p = transTime(p)
    op_s = transTime(op_s)
    op_e = transTime(op_e)

    // 명령 수행해줘
    while (commands.length) {
        let command = ''
        // 현재 위치가 오프닝 구간인지 확인해줘
        if (op_s <= p && op_e >= p) {
            p = op_e
        }
        
        // 각 명령을 수행해줘
        command = commands.shift()
        if (command === 'next') {
            if (p + 10 > v) {
                p = v
            } else {p += 10}
        } else if (command === 'prev') {
            if (p - 10 < 0) {
                p = 0
            } else {p -= 10}
        }
    }
    
    if (op_s <= p && p <= op_e) {
        p = op_e
    }
    
    const a = Math.floor(p / 60)
    const b = p % 60
    
    return String(a).padStart(2, '0')+":"+String(b).padStart(2, '0')
}