mod character;

use std::os::raw::{c_uchar, c_ulonglong};

#[no_mangle]
pub extern "C" fn roll_attributes(
    dices: c_ulonglong,
    skipped_dices: c_ulonglong,
    dice_type: c_uchar,
) -> *const c_uchar {
    character::roll_attributes(
        rand::thread_rng(),
        dices as u64,
        skipped_dices as u64,
        dice_type as u8,
    )
    .as_ptr()
}

#[no_mangle]
pub extern "C" fn roll_attribute(
    dices: c_ulonglong,
    skipped_dices: c_ulonglong,
    dice_type: c_uchar,
) -> c_uchar {
    character::roll_attribute(
        rand::thread_rng(),
        dices as u64,
        skipped_dices as u64,
        dice_type as u8,
    )
}
