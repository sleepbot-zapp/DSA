fn median_element<T: Ord>(arr: &mut [T]) -> usize{
    let first: &T = &arr[0];
    let middle: &T = &arr[arr.len() / 2];
    let last: &T = &arr[arr.len() - 1];
    if (first < middle && middle < last) || (last < middle && middle < first) {
        arr.len() / 2
    } else if (middle < first && first < last) || (last < first && first < middle) {
        0 as usize
    } else {
        arr.len() - 1
    }
}

pub fn quick_sort<T: Ord + Copy>(arr : &mut [T]){
    if arr.len() > 1{
        let pivot_index: usize = median_element(arr);
        arr.swap(pivot_index, arr.len() - 1);
        let mut i: usize = 0;
        let mut j: usize = 0;
        while j < arr.len() - 1 {
            if arr[j] < arr[arr.len() - 1] {
                arr.swap(i, j);
                i += 1;
                j += 1;
            } else {
                j += 1;
            }
        }
        arr.swap(i, arr.len() - 1);
    
        quick_sort(&mut arr[..i]);
        quick_sort(&mut arr[i+1..]);
    }
}
