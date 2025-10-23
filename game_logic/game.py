from utils import deck

def create_player(name: str ='AI') -> dict:
    return {'name': name, 'hand': [], 'won_pile': []}


def init_game() -> dict:
    player_1 = create_player("Avi")
    player_2 = create_player()
    new_deck = deck.create_deck()
    shuffled_deck = deck.shuffle(new_deck)

    player_1_hand = shuffled_deck[27:]
    player_2_hand = shuffled_deck[:27]

    player_1['hand'] = player_1_hand
    player_2['hand'] = player_2_hand

    return {
        'deck': shuffled_deck,
        'player_1': player_1,
        'player_2': player_2
    }


def play_round(p1: dict, p2: dict):
    p1_hand = p1['hand']
    p1_top_card = p1_hand[-1]

    p2_hand = p2['hand']
    p2_top_card = p2_hand[-1]

    winer = deck.compare_cards(p1_top_card, p2_top_card)
    if winer == 'p1':
        won = p2['hand'].pop()
        p1['won_pile'].append(won)
        p1['won_pile'].append(p1_hand.pop())

    if winer == 'p2':
        won = p1['hand'].pop()
        p2['won_pile'].append(won)
        p2['won_pile'].append(p2_hand.pop())
    else:
        pass
