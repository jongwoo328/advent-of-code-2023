from itertools import combinations_with_replacement


def get_type(cards: list[str]):
    sorted_cards = sorted(cards)

    def is_five_of_a_kind(cards):
        return len(set(cards)) == 1

    def is_four_of_a_kind(cards):
        return len(set(cards)) == 2 and (
            cards.count(cards[0]) == 4 or cards.count(cards[-1]) == 4
        )

    def is_full_house(cards):
        return len(set(cards)) == 2 and (
            cards.count(cards[0]) == 3 or cards.count(cards[-1]) == 3
        )

    def is_three_of_a_kind(cards):
        return len(set(cards)) == 3 and (
            cards.count(cards[0]) == 3
            or cards.count(cards[-1]) == 3
            or cards.count(cards[1]) == 3
        )

    def is_two_pairs(cards):
        return len(set(cards)) == 3 and (
            cards.count(cards[0]) == 2
            or cards.count(cards[-1]) == 2
            or cards.count(cards[2]) == 2
        )

    def is_one_pair(cards):
        return len(set(cards)) == 4 and (
            cards.count(cards[0]) == 2
            or cards.count(cards[1]) == 2
            or cards.count(cards[2]) == 2
            or cards.count(cards[3]) == 2
        )

    if is_five_of_a_kind(sorted_cards):
        return 7
    elif is_four_of_a_kind(sorted_cards):
        return 6
    elif is_full_house(sorted_cards):
        return 5
    elif is_three_of_a_kind(sorted_cards):
        return 4
    elif is_two_pairs(sorted_cards):
        return 3
    elif is_one_pair(sorted_cards):
        return 2
    else:
        return 1


card_value = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 1,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


def get_nth_card_as_value(cards: list[str], n: int):
    return card_value[cards[n - 1]]


def sort_by_max_type(cards: list[str]) -> int:
    cards_set = set(cards)
    j_cnt = cards.count("J")
    max_type = 0
    for comb in combinations_with_replacement(cards_set, j_cnt):
        new_cards = []
        comb_list = list(comb)
        for card in cards:
            if card == "J":
                new_cards.append(comb_list.pop(0))
            else:
                new_cards.append(card)
        max_type = max(max_type, get_type(new_cards))
        if max_type == 7:
            break
    return max_type


def calculate(cards_and_bids):
    sorted_data = sorted(
        cards_and_bids,
        key=lambda x: (
            -sort_by_max_type(x["cards"]),
            -get_nth_card_as_value(x["cards"], 1),
            -get_nth_card_as_value(x["cards"], 2),
            -get_nth_card_as_value(x["cards"], 3),
            -get_nth_card_as_value(x["cards"], 4),
            -get_nth_card_as_value(x["cards"], 5),
        ),
    )

    result = 0
    for index, data in enumerate(sorted_data, start=1):
        score = len(sorted_data) - index + 1
        result += score * data["bid"]
    return result


with open("day7-2.input", "r") as f:
    cards_data = f.readlines()
    cards_and_bids = [
        {
            "cards": list(card_data.split(" ")[0]),
            "bid": int(card_data.split(" ")[1]),
        }
        for card_data in cards_data
    ]

    print(calculate(cards_and_bids))
