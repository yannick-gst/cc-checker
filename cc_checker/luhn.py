#-*- coding: utf-8 -*-

def is_valid_cc_number(cc_number: str) -> bool:
    last_digit = int(cc_number[-1])
    remaining_reversed = cc_number[-2::-1]
    nums = [
        int(num) if idx % 2 != 0 \
        else int(num) * 2 if int(num) * 2 <= 9 \
        else int(num) * 2 % 10 + int(num) * 2 // 10 \
        for idx, num in enumerate(remaining_reversed)
    ]
    return (sum(nums) + last_digit) % 10 == 0
