fn merge<T: Ord + Copy>(array: &mut [T], mid: usize) {
    let left_half = array[..mid].to_vec();
    let right_half = array[mid..].to_vec();
    let mut l = 0;
    let mut r = 0;

    while l<left_half.len() && r<right_half.len(){
        if left_half[l] <= right_half[r]{
            array[r + l] = left_half[l];
            l += 1;
        } else {
            array[r + l] = right_half[r];
            r += 1;
        }
    }
    while l<left_half.len() {
        array[r + l] = left_half[l];
        l += 1;
    }
    while r<right_half.len() {
        array[r + l] = right_half[r];
        r += 1;
    }
}

pub fn merge_sort<T: Ord + Copy>(array: &mut [T]) {
    if array.len() > 1 {
        let mid = array.len() / 2;
        merge_sort(&mut array[..mid]);
        merge_sort(&mut array[mid..]);
        merge(array, mid);
    }
}