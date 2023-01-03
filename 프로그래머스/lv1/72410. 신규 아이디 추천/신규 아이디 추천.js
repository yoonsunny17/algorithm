function solution(new_id) {
    // step 1
    new_id = new_id.toLowerCase()
    
    // step 2
    new_id = new_id.replace(/[^\w\-\.]/g, '')
    
    // step 3
    new_id = new_id.replace(/\.{2,}/g, '.')
    
    // step 4
    new_id = new_id.replace(/^\.|\.$/g, '')
    
    // step 5
    if (new_id.length === 0) new_id = "a"
    
    // step 6
    if (new_id.length >= 16) new_id = new_id.slice(0, 15)
    new_id = new_id.replace(/\.$/g, '')
    
    // step 7
    if (new_id.length <= 2) new_id = new_id + new_id[new_id.length-1].repeat(3 - new_id.length)
    
    return new_id
}