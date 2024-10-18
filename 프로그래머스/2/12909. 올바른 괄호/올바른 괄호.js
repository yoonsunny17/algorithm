function solution(s){
    let stack = [];
    
    for (let i of s) {
        // 1. 스택이 비어있는데 닫힌 괄호 들어옴 > return false
        if (!stack.length && i == ')'){
            return false
        }
        // 2. 스택 마지막 원소가 열린괄호인데 닫힌 괄호 들어옴 > pop
        if (stack[stack.length - 1] == '(' && i == ')'){
            stack.pop()
        }
        // 3. 열린 괄호 들어옴 > push
        if (i == '(') {
            stack.push(i)
        }
    }

    return !stack.length ? true : false;
}