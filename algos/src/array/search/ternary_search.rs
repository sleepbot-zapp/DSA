#![allow(dead_code)]

pub fn ternary_search_recursive<T: Ord>(array: &[T], target: T, low: usize, high: usize) -> Option<usize> {
    if low > high {
        return None;
    }

    let mid1 = low + (high - low) / 3;
    let mid2 = high - (high - low) / 3;
    if array[mid1] == target {
        return Some(mid1);
    } else if array[mid2] == target {
        return Some(mid2);
    }

    if target < array[mid1] {
        ternary_search_recursive(&array, target, low, mid1 - 1)
    } else if target > array[mid2] {
        ternary_search_recursive(&array, target, mid2+1, high)
    } else {
        ternary_search_recursive(&array, target, mid1+1, mid2-1)
    }

}


pub fn ternary_search_iterative<T: Ord>(array: &[T], target: T) -> Option<usize> {
    let mut low = 0;
    let mut high = array.len() - 1;

    while low <= high {
        let mid1 = low + (high - low) / 3;
        let mid2 = high - (high - low) / 3;

        if array[mid1] == target {
            return Some(mid1);
        } else if array[mid2] == target {
            return Some(mid2);
        }

        if target < array[mid1] {
            high = mid1 - 1;
        } else if target > array[mid2] {
            low = mid2 + 1;
        } else {
            low = mid1 + 1;
            high = mid2 - 1;
        }
    }

    None
}