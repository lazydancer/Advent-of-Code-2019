use std::collections::btree_map::BTreeMap;

fn only_doubles(x: u32) -> bool {
    let mut count = BTreeMap::new();

    for c in x.to_string().chars() {
        *count.entry(c).or_insert(0) += 1
    }

    count.iter().map(|(ch, count)| count).any(|x| (*x == 2))
}

fn adjancent_chars(x: u32) -> bool {
    let x = x.to_string();
    let chars_a: Vec<_> = x.chars().collect();
    let chars_b = &chars_a.clone()[1..];

    chars_a.iter().zip(chars_b.iter()).map(|(a, b)| a == b).any(|x| x)
}

fn always_increase(x: u32) -> bool {
    let x = x.to_string();
    let chars_a: Vec<_> = x.chars().map(|x| x.to_digit(10).unwrap()).collect();
    let chars_b = &chars_a.clone()[1..];

    chars_a.iter().zip(chars_b.iter()).map(|(a, b)| a <= b).all(|x| x)
}

fn main() {

    let mut part_1_count = 0;
    for i in 387638..919123 {
        if adjancent_chars(i) && always_increase(i) {
            part_1_count += 1;
        }
    }

    println!("{:?}", part_1_count); //466

    let mut part_2_count = 0;
    for i in 387638..919123 {
        if adjancent_chars(i) && always_increase(i) && only_doubles(i) {
            part_2_count += 1;
            println!("{:?}: {:?}", part_2_count, i);
        }
    }

    println!("{:?}", part_2_count); //292

}


