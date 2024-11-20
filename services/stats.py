import json

# Получение статистики пользователя по id из JSON
async def get_data_from_json(user_id):
    with open('services/users_1.json', 'r') as file:
        try:
            user_id = str(user_id)
            dic = json.load(file)
            if user_id in dic.keys():
                return dic[user_id]
            else:
                return False
        except:
            return False

# Добавление нового пользователя в JSON или обнуление старого при сбросе статистики
async def update_user_to_database(data):

    if '544532605' in data.keys():# Проверка на аккаунт Вадима для видоса
        data['544532605']['clown'] = 0

    with open('services/users_1.json', 'r') as file:
        try:
            dic = json.load(file)
            dic.update(data)
        except:
            dic = data
    with open('services/users_1.json', 'w') as file:
        json.dump(dic, file)

# Обновление данных в статистике (после каждой игры)
async def update_user_data(user_id,**kwargs):
    data: dict = await get_data_from_json(user_id)
    if data:
        for i in kwargs.items():
            if i[0] in data.keys():
                data[i[0]] = i[1] + data[i[0]]

    if user_id == '544532605': # Проверка на аккаунт Вадима для видоса
        data['544532605']['clown'] = 0

    await update_user_to_database({str(user_id):data})


