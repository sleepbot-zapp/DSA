pub fn knuth_morris_pratt(main_str: &str, pattern_str: &str) -> isize{
    let m: usize = main_str.len();
    let n: usize = pattern_str.len();
    let mut i = 0;
    let mut j = 0;
    while i < m{
        while j < n {
            if main_str.as_bytes()[i] != pattern_str.as_bytes()[j]{
                j = 0;
                i += 1;
                break
            } else { 
                j += 1;
            }
            i += 1;
            if j == n{
                return (i-n) as isize;
            }
        }
    }
    return -1;
}