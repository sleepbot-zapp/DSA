pub fn insertion_sort<T: Ord + Copy>(array: &mut [T]) {
    for i in 1..array.len() {
        let mut j = i;
        let cur = array[i];

        while j > 0 && array[j - 1] > cur {
            array[j] = array[j - 1];
            j -= 1;
        }
        array[j] = cur;
    }
}