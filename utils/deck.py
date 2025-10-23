import random

def create_card(rank: str, suite: str) -> dict:
        try:
            value = int(rank)
        except ValueError:
            match rank:
                case 'J':
                    value = 11
                case 'Q':
                    value = 12
                case 'K':
                    value = 13
                case 'A':
                    value = 14
                case _:
                    print('Invalid rank')


        return {
            'rank': rank,
            'suite': suite,
            'value': value
        }


def compare_cards(p1_card: dict, p2_card: dict) -> str:
    winer = ''

    if p1_card['value'] > p2_card['value']:
        winer = 'p1'
    elif p2_card['value'] > p1_card['value']:
        winer = 'p2'
    else:
        winer = 'WAR'

    return winer


def create_deck() -> list[dict]:
    deck = []
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['H', 'C', 'D', 'S']

    for suite in suits:
        for rank in ranks:
            card = create_card(rank, suite)
            deck.append(card)

    return deck


def shuffle(deck: list[dict]) -> list[dict]:
    len_deck = 52

    for i in range(1000):
        index_1 = 0
        index_2 = 0

        while index_1 == index_2:
            index_1 = random.randint(0, len_deck -1)
            index_2 = random.randint(0, len_deck -1)

        deck[index_1], deck[index_2] = deck[index_2], deck[index_1]

    return deck

print("card test:", create_card('A','S'))
print("card test:",  create_card('10','H'))

print('comper test:', compare_cards( create_card('A','S'),
                               create_card('10','H')
                               )
      )

print('create_deck test:', len(create_deck()))
