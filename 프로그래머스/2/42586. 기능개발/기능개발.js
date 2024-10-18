function solution(progresses, speeds) {
  let ans = [];

  const N = progresses.length;

  let days = []; // 남은 날들 계산해서 넣어줄 리스트
  for (let i = 0; i < N; i++) {
    let leftDays = Math.ceil((100 - progresses[i]) / speeds[i]);
    days.push(leftDays);
  }

  let curr = days.shift();
  let cnt = 1;
  while (days.length > 0) {
    let tmp = days.shift();
    if (curr < tmp) {
      // 현재 기준보다 더 크면, 지금까지 cnt 넣어주고 초기화, curr 갱신
      ans.push(cnt);
      cnt = 1;
      curr = tmp;
    } else {
      // cnt++
      cnt++;
    }
  }

  if (cnt > 0) {
    ans.push(cnt);
  }

  return ans;
}