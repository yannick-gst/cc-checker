#-*- coding: utf-8 -*-

import unittest
from .context import cc_checker
from cc_checker import luhn


class TestLuhn(unittest.TestCase):
    def test_valid(self):
        # Test card number from:
        # https://en.wikipedia.org/wiki/Luhn_algorithm
        self.assertTrue(luhn.is_valid_card_number('17893729974'))

        # Test card numbers were obtained from:
        # https://support.bluesnap.com/docs/test-credit-card-numbers

        # AMEX
        self.assertTrue(luhn.is_valid_card_number('374245455400126'))
        self.assertTrue(luhn.is_valid_card_number('378282246310005'))

        # Mastercard
        self.assertTrue(luhn.is_valid_card_number('5425233430109903'))
        self.assertTrue(luhn.is_valid_card_number('2223000048410010'))

        # VISA
        self.assertTrue(luhn.is_valid_card_number('4263982640269299'))
        self.assertTrue(luhn.is_valid_card_number('4917484589897107'))
        self.assertTrue(luhn.is_valid_card_number('4001919257537193'))
        self.assertTrue(luhn.is_valid_card_number('4007702835532454'))
        self.assertTrue(luhn.is_valid_card_number('4701322211111234'))
        self.assertTrue(luhn.is_valid_card_number('4347699988887777'))

    def test_invalid(self):
        # Test card numbers are the same as in test_valid(), except the last
        # digit has been changed from the original.
        self.assertFalse(luhn.is_valid_card_number('17893729975'))
        self.assertFalse(luhn.is_valid_card_number('374245455400127'))
        self.assertFalse(luhn.is_valid_card_number('378282246310007'))
        self.assertFalse(luhn.is_valid_card_number('5425233430109900'))
        self.assertFalse(luhn.is_valid_card_number('2223000048410011'))
        self.assertFalse(luhn.is_valid_card_number('4263982640269290'))
        self.assertFalse(luhn.is_valid_card_number('4917484589897108'))
        self.assertFalse(luhn.is_valid_card_number('4001919257537194'))
        self.assertFalse(luhn.is_valid_card_number('4007702835532456'))
        self.assertFalse(luhn.is_valid_card_number('4701322211111238'))
        self.assertFalse(luhn.is_valid_card_number('4347699988887770'))

    def test_iin(self):
        self.assertEqual(
            "American Express", luhn.issuing_network('374245455400126')
        )
        self.assertEqual("Mastercard", luhn.issuing_network('5425233430109903'))
        self.assertEqual("Visa", luhn.issuing_network('4263982640269299'))
