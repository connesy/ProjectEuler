# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""
from python.utils.file_utils import read_data_file

BASE_ORD = ord("A") - 1


def get_sorted_names() -> list[str]:
    data = read_data_file(module_file_path=__file__)[0]
    cleaned_data = data.replace('"', "").split(",")
    return list(sorted(cleaned_data))


def calculate_alphabetical_value(name: str) -> int:
    return sum(ord(s) for s in name) - BASE_ORD * len(name)


def calculate_name_score(name: str, index: int) -> int:
    alphabetical_value = calculate_alphabetical_value(name)
    name_score = alphabetical_value * (index + 1)
    return name_score


if __name__ == "__main__":
    names = get_sorted_names()
    name_scores = {name: calculate_name_score(name, idx) for idx, name in enumerate(names)}
    print("COLIN", names.index("COLIN"), calculate_alphabetical_value("COLIN"), name_scores["COLIN"])
    print(sum(name_scores.values()))
