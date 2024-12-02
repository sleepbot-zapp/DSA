pub fn naive(main_str: &str, pattern_str: &str) -> isize{
    let m: usize = main_str.len();
    let n: usize = pattern_str.len();
    let mut j: usize = 0;
    for i in 0..=m-n{
        while j < n {
            if main_str.as_bytes()[i+j] != pattern_str.as_bytes()[j]{
                break;
            }
            j += 1;
        }
        if j == n{
            return i as isize;
        }
        j = 0;
    }
    return -1;
}