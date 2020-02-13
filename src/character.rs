use rand::Rng;

pub fn roll_attributes<R: Rng + Copy>(
    rng: R,
    dices: u64,
    skipped_dices: u64,
    dice_type: u8,
) -> Vec<u8> {
    (0..6)
        .map(|_| roll_attribute(rng, dices, skipped_dices, dice_type))
        .collect()
}

pub fn roll_attribute<R: Rng + Copy>(
    mut rng: R,
    dices: u64,
    skipped_dices: u64,
    dice_type: u8,
) -> u8 {
    let mut rolls: Vec<u8> = (0..dices)
        .map(|_| 1 + rng.gen_range(0, dice_type))
        .collect();
    rolls.sort();
    rolls[skipped_dices as usize..].iter().sum()
}
