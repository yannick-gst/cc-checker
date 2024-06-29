#-*- coding: utf-8 -*-

def is_valid_card_number(card_number: str) -> bool:
    if not card_number.isdigit():
        raise ValueError(f'{card_number} is not a positive number.')

    last_digit = int(card_number[-1])
    remaining_reversed = card_number[-2::-1]

    nums = [
        int(num) if idx % 2 != 0 \
        else int(num) * 2 if int(num) * 2 <= 9 \
        else int(num) * 2 % 10 + int(num) * 2 // 10 \
        for idx, num in enumerate(remaining_reversed)
    ]

    return (sum(nums) + last_digit) % 10 == 0


def issuing_network(card_number: str) -> str:
    # Dictionary mapping Issuer Identification Number (IIN) ranges to card
    # networks
    # TODO: Add more networks
    iin_ranges = {
        "American Express": [(34000000, 34999999), (37000000, 37999999)],
        "Diners Club": [
            (30000000, 30599999), (36000000, 36999999), (38000000, 39999999)
        ],
        "Discover": [
            (60110000, 60119999), (64400000, 64999999), (65000000, 65999999)
        ],
        "JCB": [(35280000, 35899999)],
        "Mastercard": [(51000000, 55999999)],
        "Visa": [(40000000, 49999999)]
    }

    first_eight = int(card_number[:8])

    for network, ranges in iin_ranges.items():
        for start, end in ranges:
            if start <= first_eight <= end:
                return network

    return "Unknown"
