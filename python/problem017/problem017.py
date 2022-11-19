# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""

ONES = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}
TEENS = {
    0: "",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}
TENS = {
    0: "",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}


def number_to_words(number: int) -> str:
    if number < 10:
        return ONES[number]

    if 10 <= number < 20:
        return TEENS[number]

    digits = list(int(d) for d in str(number))
    if 20 <= number < 100:
        tens, ones = digits
        return TENS[10 * tens] + ONES[ones]

    if 100 <= number < 1000:
        hundreds, tens, ones = digits
        tens_and_ones = number_to_words(tens * 10 + ones)
        words = f"{ONES[hundreds]} hundred"
        if tens_and_ones:
            words += f" and {tens_and_ones}"
        return words

    if number == 1000:
        return "one thousand"

    return ""


if __name__ == "__main__":
    total_letters = 0
    for i in range(1, 1001):
        words = number_to_words(i)
        letters = len(words.replace(" ", ""))
        print(i, letters, words)
        total_letters += letters

    print("Total letters: ", total_letters)
