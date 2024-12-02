pub fn linear_search<T: Ord>(array: &[T], target: T) -> Option<usize>{
    for i in 0..array.len(){
        if array[i] == target{
            return Some(i);
        }
    }
    return None;
}