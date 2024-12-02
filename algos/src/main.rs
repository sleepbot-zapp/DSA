//traits
#![allow(unused_imports)]
#![allow(dead_code)]
#![allow(unused_mut)]

//modules
mod array;
mod structures;
mod string;

//imports
use array::search::*;
use array::sort::*;
use structures::*;
use string::*;
use structures::*;

fn main() {
    // let mut a: [i32; 3] = [1, 2, 3];
    // let f: i32 = match interpolation_search::interpolation(&a, 3 as i32, 0 as usize, 3 as usize){
    //     Some(e) => e as i32,
    //     None => -1
    // };
    //
    // let mut unsorted_data = vec![3, 2,yABCjk 14, 3, 5, 6, 1];
    // exchange_sort::exchange_sort(&mut unsorted_data);
    // println!("Sorted data: {:?}", unsorted_data);
    //
    let a = String::from("xABC");
    let b = String::from("xABC");
    //let c: isize = 
    let c = boyer_moore::boyer_moore(&a, &b);
    println!("{}", c);
}
