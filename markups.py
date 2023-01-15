from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# ---------------------------------------------------------- #
buttonStart = KeyboardButton('/start')
buttonRead = KeyboardButton('/readme')
grandMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(buttonStart, buttonRead)
back_btn = KeyboardButton('/back<')
# --- grops menu --- #
btn_wheat_pears_pasta = KeyboardButton('/Борошно_крупи_макарони')
btn_conserv = KeyboardButton('/Овочі_консервовані')
btn_med_djam = KeyboardButton('/Мед_Джем')
btn_meet_fish = KeyboardButton('/Мясо_Риба')
btn_spec = KeyboardButton('/Спеції')
btn_bread = KeyboardButton('/Хліб')
btn_vegetables = KeyboardButton('/Овочі')
btn_milk_prod = KeyboardButton('/Молочна_прод')
groop_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_wheat_pears_pasta).insert(btn_conserv).insert(btn_med_djam).add(btn_meet_fish).insert(btn_spec).insert(btn_bread).add(btn_vegetables).insert(btn_milk_prod) #.insert(btn_bread)
# --- btn_wheat_pears_pasta menu --- #
btn_rice = KeyboardButton('/Крупа_рис')
btn_buckwheat = KeyboardButton('/Крупа_гречана')
btn_bulgur = KeyboardButton('/Крупа_булгур')
btn_corn = KeyboardButton('/Крупа_кукурудзяна')
#btn_manna = KeyboardButton('/Крупа_манна')
btn_vivs = KeyboardButton('/Крупа_вівсяна')
btn_pearl = KeyboardButton('/Крупа_перлова')
btn_wheat = KeyboardButton('/Крупа_пшенична')
btn_pears = KeyboardButton('/Крупа_пшоно')
btn_barley = KeyboardButton('/Крупа_ячнева')
btn_pasta = KeyboardButton('/Макаронні_вироби')
btn_wheat_f1 = KeyboardButton('/Борошно_І_гатунку')
btn_wheat_pears_pasta_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_rice).insert(btn_buckwheat).insert(btn_bulgur).add(btn_corn).insert(btn_wheat_f1).insert(btn_vivs).add(btn_pearl).insert(btn_wheat).insert(btn_pears).add(btn_barley).insert(btn_pasta).insert(back_btn)
# --- btn_conserv menu --- #
btn_goroshek = KeyboardButton('/Горошок_консервований')
btn_ikra = KeyboardButton('/Овочева_ікра')
btn_ogirky = KeyboardButton('/Огірки_консервовані')
btn_pomidory = KeyboardButton('/Помідори_консервовані')
btn_conserv_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_goroshek).insert(btn_ikra).add(btn_pomidory).insert(btn_ogirky).add(back_btn)
# --- btn_med_jam_menu --- #
btn_med = KeyboardButton('/Мед')
btn_jam = KeyboardButton('/Джем')
btn_med_jam_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_goroshek).insert(btn_ikra).add(back_btn)
# --- btn_meet_fish_menu --- #
btn_meet_chicken = KeyboardButton('/Мясо_курки')
btn_fish_hake = KeyboardButton('/Риба_Хек')
btn_cons_fish_sard = KeyboardButton('/Конс_рибна_Сардина')
btn_cons_fish_kilka = KeyboardButton('/Конс_рибна_Бички')
btn_meet_fish_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_meet_chicken).insert(btn_fish_hake).add(btn_cons_fish_sard).insert(btn_cons_fish_kilka).add(back_btn)
# --- btn_spec_menu --- #
btn_lavr = KeyboardButton('/Лавровий_лист')
btn_g_porokh = KeyboardButton('/Гірчичий_порошок')
btn_perec = KeyboardButton('/Перець_мелений')
btn_salt = KeyboardButton('/Сіль')
btn_sugar = KeyboardButton('/Цукор')
btn_spec_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_lavr).insert(btn_g_porokh).add(btn_perec).insert(btn_salt).add(btn_sugar).add(back_btn)
# --- btn_bread_menu --- #
btn_bread = KeyboardButton('/Хліб_пшен')
btn_bread_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_bread).add(back_btn)
# --- btn_vegetables_menu --- #
btn_vegetables = KeyboardButton('/Картопля')
btn_vegetables_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_vegetables).add(back_btn)
# --- btn_milk_prod_menu --- #
btn_butter = KeyboardButton('/Масло_вершкове')
btn_cheeze = KeyboardButton('/Сири_тверді')
btn_milk_prod_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_butter).insert(btn_cheeze).add(back_btn)
