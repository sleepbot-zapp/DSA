use std::cmp;

pub fn jump_search<T: Ord>(arr: &[T], target: T) -> Option<usize>{
    let n = arr.len();
    let step = (n as f64).sqrt() as usize;
    let mut prev = 0;
    let mut current = cmp::min(step, n) - 1;
    while arr[current] < target {
        prev = current;
        current += step;

        if prev >= n {
            return None;
        }
    }

    for i in prev..cmp::min(current + 1, n) {
        if arr[i] == target {
            return Some(i);
        }
    }
    None
}
