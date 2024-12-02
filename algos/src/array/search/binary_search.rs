#![allow(dead_code)]

pub fn binary_search_recursive<T: Ord>(array: &[T], target: T, low: usize, high: usize) -> Option<usize> {
    if low > high {
        return None;
    }

    let mid = low + (high - low) / 2;

    if array[mid] == target {
        Some(mid)
    } else if array[mid] > target {
        binary_search_recursive(array, target, low, mid - 1)
    } else {
        binary_search_recursive(array, target, mid + 1, high)
    }
}

pub fn binary_search_iterative<T: Ord>(array: &[T], target: T) -> Option<usize> {
    let mut low = 0;
    let mut high = array.len() - 1;

    while low <= high {
        let mid = low + (high - low) / 2;

        if array[mid] == target {
            return Some(mid);
        } else if array[mid] > target {
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    return None;
}