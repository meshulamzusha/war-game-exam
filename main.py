from game_logic import game

if __name__ == "__main__":
    game_objects = game.init_game()
    p1 = game_objects['player_1']
    p2 = game_objects['player_2']

    while p1['hand'] != 0 and p2['hand'] != 0:
        game.play_round(p1, p2)

    if len(p1['hand']) == 0 or len(p1['hand']) == 0:
        if len(p1['won_pile']) > len(p2['won_pil']):
            winer = 'p1'
        if len(p1['won_pile']) < len(p2['won_pil']):
            winer = 'p2'
        else:
            winer = 'draw'

        print(winer)