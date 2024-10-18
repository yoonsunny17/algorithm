function solution(priorities, location) {
  let q = priorities.map((val, idx) => [idx, val]);
  let ans = 0;

  while (q.length) {
    let [idx, priority] = q.shift();

    // 큐에서 우선순위가 더 높은 프로세스가 있는지 확인
    if (q.some((item) => item[1] > priority)) {
      q.push([idx, priority]);
    } else {
      ans++;
      if (idx === location) {
        return ans;
      }
    }
  }
}
