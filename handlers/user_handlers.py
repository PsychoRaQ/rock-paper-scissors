from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU, stats_generator
from aiogram import Router, F
from Keyboard import Keyboard
from aiogram.filters import or_f
from config_data import config
from services import game_process, stats


router = Router()

# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    if await stats.get_data_from_json(message.from_user.id) == False:
         await stats.update_user_to_database(data={message.from_user.id:config.DEFAULT_USERDATA})
    await message.answer(text=LEXICON_RU["let_game"],
                         reply_markup=Keyboard.keyboard_generator(config.MAIN_MENU).as_markup(resize_keyboard=True))

# Этот хэндлер срабатывает на команду /help или сообщение "Помощь"
@router.message(Command(commands='help'))
@router.message(F.text == 'Помощь')
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])

# Этот хэндлер срабатывает на команду /stats или сообщение "Посмотреть статистику"
@router.message(Command(commands='stats'))
@router.message(F.text == 'Посмотреть статистику')
async def process_stats_command(message: Message):
    data = await stats.get_data_from_json(message.from_user.id)
    if data:
        await message.answer(text=await stats_generator(data))
    else:
        await message.answer(text='Статистика не найдена.\nНапиши /start чтобы добавить свой аккаунт в базу.')

# Этот хэндлер срабатывает на команду /unstats или сообщение "Сбросить статистику"
@router.message(Command(commands='unstats'))
@router.message(F.text == 'Сбросить статистику')
async def process_unstats_command(message: Message):
    await stats.update_user_to_database({str(message.from_user.id):config.DEFAULT_USERDATA})
    await message.answer(text=LEXICON_RU['/unstats'])

# Этот хэндлер срабатывает на "Давай!"
@router.message(F.text == LEXICON_RU['go_game'])
async def process_start_game_command(message: Message):
    await message.answer(text=LEXICON_RU["start_game"],
                         reply_markup=Keyboard.keyboard_generator(config.GAME_DICT).as_markup(resize_keyboard=True) )

# Этот хэндлер срабатывает на "Не хочу!"
@router.message(F.text == LEXICON_RU['dont_game'])
async def process_no_game_command(message: Message):
    await message.answer(text=LEXICON_RU['no_game'], reply_markup=ReplyKeyboardRemove())

# Хэндлер для обработки выбора пользователя во время игры
@router.message(F.text.in_([LEXICON_RU['rock'],
                            LEXICON_RU['paper'],
                            LEXICON_RU['scissors']]))
async def process_in_game_command(message: Message):
    await message.answer(text=await game_process.game(message.text, message.from_user.id), reply_markup=Keyboard.keyboard_generator(config.MAIN_MENU).as_markup(resize_keyboard=True))
    await message.answer(text=LEXICON_RU['go_new_game'])


