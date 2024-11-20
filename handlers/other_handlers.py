from aiogram.types import Message, FSInputFile
from lexicon.lexicon import LEXICON_RU
from aiogram import Router
from services import stats

router = Router()

#Хэндлер отвечает за отправку видео для Вадима
@router.message(lambda message: message.from_user.id == 544532605)
async def send_video(message: Message):
        video = FSInputFile('mell.mp4')
        await stats.update_user_data(544532605, clown=1)
        await message.answer_video(video=video)

#Хэндлер отвечает за все остальное
@router.message()
async def send_echo(message: Message):
        await message.answer(text=LEXICON_RU['random_msg'])

