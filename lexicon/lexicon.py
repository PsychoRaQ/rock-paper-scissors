# тексты для хэндлеров
LEXICON_RU: dict[str, str] = {
    '/help': 'Здесь правила игры - Камень, Ножницы, Бумага',
    'start_game': "Отлично! Делай свой выбор!",
    'let_game': 'Давай сыграем в игру Камень, Ножницы, Бумага?',
    'no_game': 'Хорошо. Если, вдруг, захочешь сыграть - напиши команду /start',
    'random_msg': 'Я тебя не понимаю! Давай общаться кнопками?',
    '/unstats':'Статистика сброшена.'
}

# функция генерации текста для показа статистики пользователю
async def stats_generator(data):
    result = f'Ваша статистика:\n\n'\
             f'Всего матчей: {str(data['total_games'])}\n'\
             f'Побед: {str(data['wins'])}\n'\
             f'Поражений: {str(data['lose'])}\n'\
             f'Ничьих: {str(data['draw'])}\n'
    try:
        if data['clown'] != 0:
            result += f'Долбоеб: {str(data['clown'])}\n'
    except:
        pass

    return result