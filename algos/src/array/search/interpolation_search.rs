use std::ops::Sub;

pub fn interpolation<T: Ord + std::ops::Sub>(array: &[T], target: T, high: usize, low: usize) -> Option<usize>{
    if (low<= high) && (target >= array[low]) && (target <= array[high]){
        let pos: usize = low + ((high - low) / (array[high] - array[low]) * (target - array[low])) as usize;
        if array[pos] == target{
            return Some(pos);
        } else if array[pos] < target{
            interpolation(array, target, pos + 1, high);
        } else {
            interpolation(array, target, low, pos - 1);
        }
    }
    return None
}