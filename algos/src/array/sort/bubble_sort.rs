pub fn bubble_sort<T: Ord>(array: &mut [T]){
    for i in 0..array.len(){
        for j in 0..array.len()-i-1{
            if array[j] > array[j+1]{
                array.swap(j, j+1)
            }
        }
    }
}