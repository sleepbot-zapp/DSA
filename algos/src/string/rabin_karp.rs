pub fn rabin_karp(main_str: &str, pattern_str: &str) -> isize{
    let m: usize = main_str.len();
    let n: usize = pattern_str.len();
    let mut pattern_ascii_array: Vec<u128> = vec![];
    for i in 0..n{
        pattern_ascii_array.push((pattern_str.as_bytes()[i] as u128)*10_u128.pow((n-i) as u32));
    }
    let pattern_sum: u128 = pattern_ascii_array.iter().sum();

    let mut main_ascii_array: Vec<u128> = vec![];

    for i in 0..=m-n{
        main_ascii_array.clear();
        for j in 0..n{
            main_ascii_array.push((main_str.as_bytes()[i+j] as u128)*10_u128.pow((n-j) as u32));
        }
        let main_sum: u128 = main_ascii_array.iter().sum();
        if main_sum==pattern_sum{
            return i as isize;
        }
    }
    return -1;
}