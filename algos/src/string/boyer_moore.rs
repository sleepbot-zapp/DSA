pub fn boyer_moore(main_str: &str, pattern_str: &str) -> isize{
    let m: usize = main_str.len();
    let n: usize = pattern_str.len();
    let mut i: usize = 0;
    let mut j: usize = 1;
    while i < m {
        if main_str.as_bytes()[i] == pattern_str.as_bytes()[0] {
            while j < n {
                if main_str.as_bytes()[i + j] == pattern_str.as_bytes()[j] {
                    j += 1;
                } else {
                    i += j;
                    j = 0;
                    break;
                }
                if j == n - 1{
                    return i as isize;
                }
            }
        } else {
            i += 1;
        }
    }
    return -1;
}