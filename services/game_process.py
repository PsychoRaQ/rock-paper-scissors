from config_data import config
from random import randint
from services import stats
from lexicon import lexicon

# Основная логика работы игры
async def game(player, user_id) -> str:
    result = None
    BOT_SCORE = randint(1,3)
    rules = {lexicon.LEXICON_RU['rock']:1, lexicon.LEXICON_RU['scissors']: 2, lexicon.LEXICON_RU['paper']: 3}
    bot_chosen = config.GAME_DICT[BOT_SCORE-1]
    player_score = rules[player]

    player_win = f'Выбор бота: {bot_chosen}\nВыбор игрока:{player}\n\nИгрок выиграл!'
    bot_win = f'Выбор бота:{bot_chosen}\nВыбор игрока:{player}\n\nБот выиграл!'

    if BOT_SCORE == player_score:
        result = f'Выбор бота:{bot_chosen}\nВыбор игрока:{player}\nНичья!'
    elif player_score == 3:
        if BOT_SCORE == 1:
            result = player_win
        else:
            result = bot_win
    elif player_score == 2:
        if BOT_SCORE == 3:
            result = player_win
        else:
            result = bot_win
    elif player_score == 1:
        if BOT_SCORE == 2:
            result = player_win
        else:
            result = bot_win

    if result == bot_win:
        await stats.update_user_data(user_id, total_games=1, lose=1)
    elif result == player_win:
        await stats.update_user_data(user_id, total_games=1, wins=1)
    else:
        await stats.update_user_data(user_id, total_games=1, draw=1)

    return result