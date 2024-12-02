pub fn stalin_sort<T: Ord>(arr: &mut Vec<T>){
    let mut removes = 0;
    for i in 0..(arr.len()-1){
        if arr[i-removes] > arr[i-removes+1]{
            arr.remove(i-removes+1);
            removes += 1;
        }
    }
}