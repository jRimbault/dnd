import argparse
import ctypes
import os
import random
import typing

dnd = ctypes.cdll.LoadLibrary(os.path.join("target", "debug", "libdnd.so"))
dnd.roll_attribute.restype = ctypes.c_uint8
dnd.roll_attributes.restype = ctypes.POINTER(ctypes.c_uint8)


def roll_attributes(dices: int, skipped_dices: int, dice_type: int):
    yield from (dnd.roll_attribute(dices, skipped_dices, dice_type) for _ in range(6))


print(*roll_attributes(5, 2, 6))

p = dnd.roll_attributes(5, 2, 6)
print(*[p[i] for i in range(6)])
