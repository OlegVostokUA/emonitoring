from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from main_func import send_message

import markups as mkps

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())
storage = MemoryStorage()

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("GO!", reply_markup = mkps.groop_menu)

@dp.message_handler(commands=['readme'])
async def process_help_command(message: types.Message):
    await message.reply("about bot and developer", reply_markup = mkps.grandMenu)

@dp.message_handler(commands=['back<'])
async def process_start_command(message: types.Message):
    await message.reply("GO!", reply_markup = mkps.groop_menu)

@dp.message_handler(commands=['Борошно_крупи_макарони'])
async def process_help_command(message: types.Message):
    await message.reply("ok ", reply_markup = mkps.btn_wheat_pears_pasta_menu)

@dp.message_handler(commands=['Овочі_консервовані'])
async def process_help_command(message: types.Message):
    await message.reply("ok ", reply_markup = mkps.btn_conserv_menu)

@dp.message_handler(commands=['Мед_Джем'])
async def process_help_command(message: types.Message):
    await message.reply("ok ", reply_markup = mkps.btn_med_jam_menu)

@dp.message_handler(commands=['Мясо_Риба'])
async def process_help_command(message: types.Message):
    await message.reply("ok ", reply_markup = mkps.btn_meet_fish_menu)

@dp.message_handler(commands=['Спеції'])
async def process_help_command(message: types.Message):
    await message.reply("ok ", reply_markup = mkps.btn_spec_menu)

@dp.message_handler(commands=['Хліб'])
async def process_help_command(message: types.Message):
    await message.reply("ok ", reply_markup = mkps.btn_bread_menu)

@dp.message_handler(commands=['Овочі'])
async def process_help_command(message: types.Message):
    await message.reply("ok ", reply_markup = mkps.btn_vegetables_menu)

@dp.message_handler(commands=['Молочна_прод'])
async def process_help_command(message: types.Message):
    await message.reply("ok ", reply_markup = mkps.btn_milk_prod_menu)
### --- handlers --- ###

@dp.message_handler(commands=['Крупа_гречана'])
async def grechka(message: types.Message):
    resp = "/Крупа_гречана"
    mess_for_client = send_message(resp)
    await bot.send_message(message.from_user.id, mess_for_client)

@dp.message_handler(commands=['Крупа_рис'])
async def ris(message: types.Message):
    resp = "/Крупа_рис"
    mess_for_client = send_message(resp)
    await bot.send_message(message.from_user.id, mess_for_client)


@dp.message_handler(commands=['Крупа_булгур'])
async def bulgur(message: types.Message):
    resp = "/Крупа_булгур"
    mess_for_client = send_message(resp)
    await bot.send_message(message.from_user.id, mess_for_client)


@dp.message_handler(commands=['Крупа_кукурудзяна'])
async def corn(message: types.Message):
    resp = "/Крупа_кукурудзяна"
    mess_for_client = send_message(resp)
    await bot.send_message(message.from_user.id, mess_for_client)


@dp.message_handler(commands=['Крупа_гречана'])
async def grechka(message: types.Message):
    resp = "/Крупа_гречана"
    mess_for_client = send_message(resp)
    await bot.send_message(message.from_user.id, mess_for_client)


@dp.message_handler(commands=['Крупа_вівсяна'])
async def ovsan(message: types.Message):
    resp = "/Крупа_вівсяна"
    mess_for_client = send_message(resp)
    await bot.send_message(message.from_user.id, mess_for_client)


@dp.message_handler(commands=['Крупа_перлова'])
async def perlov(message: types.Message):
    resp = "/Крупа_перлова"
    mess_for_client = send_message(resp)
    await bot.send_message(message.from_user.id, mess_for_client)


@dp.message_handler(commands=['Крупа_пшенична'])
async def pshen(message: types.Message):
    resp = "/Крупа_пшенична"
    mess_for_client = send_message(resp)
    await bot.send_message(message.from_user.id, mess_for_client)


@dp.message_handler(commands=['Крупа_пшоно'])
async def pshono(message: types.Message):
    resp = "/Крупа_пшоно"
    mess_for_client = send_message(resp)
    await bot.send_message(message.from_user.id, mess_for_client)


@dp.message_handler(commands=['Крупа_ячнева'])
async def yachnev(message: types.Message):
    resp = "/Крупа_ячнева"
    mess_for_client = send_message(resp)
    await bot.send_message(message.from_user.id, mess_for_client)


@dp.message_handler(commands=['Макаронні_вироби'])
async def macaron(message: types.Message):
    resp = "/Макаронні_вироби"
    mess_for_client = send_message(resp)
    await bot.send_message(message.from_user.id, mess_for_client)


@dp.message_handler(commands=['Крупа_гречана'])
async def grechka(message: types.Message):
    resp = "/Крупа_гречана"
    mess_for_client = send_message(resp)
    await bot.send_message(message.from_user.id, mess_for_client)


@dp.message_handler(commands=['Борошно_І_гатунку'])
async def boroshn(message: types.Message):
    resp = "/Борошно_І_гатунку"
    mess_for_client = send_message(resp)
    await bot.send_message(message.from_user.id, mess_for_client)


@dp.message_handler(commands=['Олія'])
async def oil(message: types.Message):
    resp = "/Олія"
    mess_for_client = send_message(resp)
    await bot.send_message(message.from_user.id, mess_for_client)


@dp.message_handler(commands=['Горошок_консервований'])
async def goroshek(message: types.Message):
    resp = "/Горошок_консервований"
    mess_for_client = send_message(resp)
    await bot.send_message(message.from_user.id, mess_for_client)


@dp.message_handler(commands=['Овочева_ікра'])
async def icra_veg(message: types.Message):
    resp = "/Овочева_ікра"
    mess_for_client = send_message(resp)
    await bot.send_message(message.from_user.id, mess_for_client)


@dp.message_handler(commands=['Крупа_гречана'])
async def grechka(message: types.Message):
    resp = "/Крупа_гречана"
    mess_for_client = send_message(resp)
    await bot.send_message(message.from_user.id, mess_for_client)


@dp.message_handler(commands=['Огірки_консервовані'])
async def ogurc_c(message: types.Message):
    resp = "/Огірки_консервовані"
    mess_for_client = send_message(resp)
    await bot.send_message(message.from_user.id, mess_for_client)


@dp.message_handler(commands=['Помідори_консервовані'])
async def pomid_c(message: types.Message):
    resp = "/Помідори_консервовані"
    mess_for_client = send_message(resp)
    await bot.send_message(message.from_user.id, mess_for_client)


@dp.message_handler(commands=['Мед'])
async def med(message: types.Message):
    resp = "/Мед"
    mess_for_client = send_message(resp)
    await bot.send_message(message.from_user.id, mess_for_client)

@dp.message_handler(commands=['Джем'])
async def jam(message: types.Message):
    resp = "/Джем"
    mess_for_client = send_message(resp)
    await bot.send_message(message.from_user.id, mess_for_client)

@dp.message_handler(commands=['Конс_рибна_Бички'])
async def cons_fish_s(message: types.Message):
    resp = "/Конс_рибна_Бички"
    mess_for_client = send_message(resp)
    await bot.send_message(message.from_user.id, mess_for_client)

@dp.message_handler(commands=['Конс_рибна_Сардина'])
async def cons_fish_k(message: types.Message):
    resp = "/Конс_рибна_Сардина"
    mess_for_client = send_message(resp)
    await bot.send_message(message.from_user.id, mess_for_client)

@dp.message_handler(commands=['Мясо_курки'])
async def meat_chick(message: types.Message):
    resp = "/Мясо_курки"
    mess_for_client = send_message(resp)
    await bot.send_message(message.from_user.id, mess_for_client)

@dp.message_handler(commands=['Риба_Хек'])
async def fish_hake(message: types.Message):
    resp = "/Риба_Хек"
    mess_for_client = send_message(resp)
    await bot.send_message(message.from_user.id, mess_for_client)

@dp.message_handler(commands=['Лавровий_лист'])
async def lavr(message: types.Message):
    resp = "/Лавровий_лист"
    mess_for_client = send_message(resp)
    await bot.send_message(message.from_user.id, mess_for_client)

@dp.message_handler(commands=['Гірчичий_порошок'])
async def g_porokh(message: types.Message):
    resp = "/Гірчичий_порошок"
    mess_for_client = send_message(resp)
    await bot.send_message(message.from_user.id, mess_for_client)

@dp.message_handler(commands=['Перець_мелений'])
async def perec(message: types.Message):
    resp = "/Перець_мелений"
    mess_for_client = send_message(resp)
    await bot.send_message(message.from_user.id, mess_for_client)

@dp.message_handler(commands=['Сіль'])
async def salt(message: types.Message):
    resp = "/Сіль"
    mess_for_client = send_message(resp)
    await bot.send_message(message.from_user.id, mess_for_client)

@dp.message_handler(commands=['Цукор'])
async def sugar(message: types.Message):
    resp = "/Цукор"
    mess_for_client = send_message(resp)
    await bot.send_message(message.from_user.id, mess_for_client)

@dp.message_handler(commands=['Хліб_пшен'])
async def bread(message: types.Message):
    resp = "/Хліб_пшен"
    mess_for_client = send_message(resp)
    await bot.send_message(message.from_user.id, mess_for_client)

@dp.message_handler(commands=['Картопля'])
async def vegetabl(message: types.Message):
    resp = "/Картопля"
    mess_for_client = send_message(resp)
    await bot.send_message(message.from_user.id, mess_for_client)

@dp.message_handler(commands=['Сири_тверді'])
async def cheeze(message: types.Message):
    resp = "/Сири_тверді"
    mess_for_client = send_message(resp)
    await bot.send_message(message.from_user.id, mess_for_client)

@dp.message_handler(commands=['Масло_вершкове'])
async def butter(message: types.Message):
    resp = "/Масло_вершкове"
    mess_for_client = send_message(resp)
    await bot.send_message(message.from_user.id, mess_for_client)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)