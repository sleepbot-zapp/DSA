pub fn sentinel_linear_search<T: Ord + Copy>(array: &mut [T], target: T) -> Option<usize>{
    let n = array.len();
    let last = array[n - 1];
    array[n - 1] = target;
    let mut i = 0;
    while array[i] != target{
        i += 1
    };
    array[n - 1] = last;
    if (i < n - 1) | (array[n - 1] == target){
        return Some(i);
    };
    return None;
}