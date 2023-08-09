function solution(n, m, section) {
    let ans = 0;
    
    let range = 0; // 현재까지 칠한 구역
    
    section.forEach((n) => {
        // 칠해야 하는 구역의 숫자가, 지금까지 칠한 구역 숫자보다 더 크다면
        if (n > range) {
            // 구역을 칠해주고 현재까지 칠한 구역을 업데이트 시키기
            range = n + m - 1;
            
            // 페인트 칠했으니 1 증가 시키기
            ans++
        }
    });
    
    return ans;
}