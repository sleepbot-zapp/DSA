pub fn exchange_sort<T : Ord>(arr: &mut [T]) {
    let len: usize = arr.len();
    for number1 in 0..len {
        for number2 in (number1 + 1)..len {
            if arr[number2] < arr[number1] {
                arr.swap(number1, number2)
            }
        }
    }
}